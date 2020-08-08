import sys

class Node(object):
  def __init__(self, value, frequency=1, children=[None, None]):
    self.value = value
    self.frequency = frequency
    self.children = children

class TreeNode(object):
  def __init__(self, value, frequency=1, left=None, right=None):
    self.value = value
    self.frequency = frequency
    self.left = left
    self.right = right
    self.left_bit = "0"
    self.right_bit = "1"

class HuffmanTree(object):
  def __init__(self, root=None):
    self.root = root

# Binary tree: Implemented using an array
class MinHeap(object):
  def __init__(self, initial_size=10):
    self.heap = [None for _ in range(initial_size)]
    self.next_index = 0

  def size(self):
    return self.next_index

  def insert(self, node):
    # insert new element
    self.heap[self.next_index] = node

    # up-heapify as needed
    child_index = self.next_index
    parent_index = (child_index - 1) // 2

    # while we haven't reached our root node and our child node frequency is of a smaller value than our parent frequency, swap the parent and child values and move up our tree
    while child_index > 0 and self.heap[child_index].frequency < self.heap[parent_index].frequency:
      # extract value, frequency, and children properties from nodes
      child_values = (self.heap[child_index].value, self.heap[child_index].frequency, self.heap[child_index].children)
      parent_values = (self.heap[parent_index].value, self.heap[parent_index].frequency, self.heap[parent_index].children)

      # swap parent and child value, frequency, and children propertie to ensure the node with smallest frequency is the parent
      self.heap[parent_index].value = child_values[0]
      self.heap[parent_index].frequency = child_values[1]
      self.heap[parent_index].children = child_values[2]

      self.heap[child_index].value = parent_values[0]
      self.heap[child_index].frequency = parent_values[1]
      self.heap[child_index].children = parent_values[2]

      # update parent and child indexes to move up the heap
      child_index = parent_index
      parent_index = (child_index - 1) // 2

    # if, after inserting our new node, we've reached capacity, expand the heap
    if self.next_index == len(self.heap) - 1:
      self.expand()

    # increment next_index
    self.next_index += 1

  def remove(self):
    # extract root element
    node_to_remove = Node(self.heap[0].value, self.heap[0].frequency, self.heap[0].children)

    # move last element values to root
    self.heap[0].value = self.heap[self.next_index - 1].value
    self.heap[0].frequency = self.heap[self.next_index - 1].frequency
    self.heap[0].children = self.heap[self.next_index - 1].children

    # reset last element to None
    self.heap[self.next_index - 1] = None
    # decrement next_index
    self.next_index -= 1

    # down-heapify as needed
    parent_index = 0

    # explore the heap while we still have values to visit
    while parent_index < self.next_index:
      parent_values = (self.heap[parent_index].value, self.heap[parent_index].frequency, self.heap[parent_index].children)
      new_values = None

      left_child_index = 2 * parent_index + 1
      right_child_index = 2 * parent_index + 2

      # check left child
      if self.heap[left_child_index]:
        new_values = (self.heap[left_child_index].value, self.heap[left_child_index].frequency, self.heap[left_child_index].children)

      # check right child
      if self.heap[right_child_index]:
        min_freq = min(new_values[1], self.heap[right_child_index].frequency)
        if min_freq != new_values[1]:
          new_values = (self.heap[right_child_index].value, self.heap[right_child_index].frequency, self.heap[right_child_index].children)

      # if our new_values are different from our current parent values, verify which child node needs to be switched with our parent, do the switch, and update our parent index to the child index for the node we switched with to continue our down-heapify.
      if new_values and parent_values[1] > new_values[1]:
        self.heap[parent_index].value = new_values[0]
        self.heap[parent_index].frequency = new_values[1]
        self.heap[parent_index].children = new_values[2]

        # if our new_values came from our left child, update our left child
        if self.heap[left_child_index] and self.heap[left_child_index].value == new_values[0] and self.heap[left_child_index].frequency == new_values[1]:
          self.heap[left_child_index].value = parent_values[0]
          self.heap[left_child_index].frequency = parent_values[1]
          self.heap[left_child_index].children = parent_values[2]
          parent_index = left_child_index
        else:
          # our new_values came from our right child, so update our right child
          self.heap[right_child_index].value = parent_values[0]
          self.heap[right_child_index].frequency = parent_values[1]
          self.heap[right_child_index].children = parent_values[2]
          parent_index = right_child_index
      else:
        # if our parent is the min element, stop down-heapifying
        break

    return node_to_remove

  def expand(self):
    prev_heap = self.heap
    self.heap = [None for _ in range(len(prev_heap) * 2)]

    for i in range(len(prev_heap)):
      self.heap[i] = prev_heap[i]

def huffman_encoding(data):
  if len(data) == 0:
    return ("", HuffmanTree().root)

  # Phase 1: Build the Huffman Tree
  # 1. Determine the frequency of each character in the message
  frequencies = get_frequencies(data)

  # 2. Create a node for each character containing: value, frequency, left child, right child
  nodes = create_nodes(frequencies)

  # 3. Create a priority queue containing each node (character) - implement this as a min-heap, sorted based on the frequency of each node
  min_heap = create_min_heap(nodes)

  # 4 Repeat Steps 4.a - 4.c until there is only 1 element left in the priorty queue
  while min_heap.heap[1]:
    # 4.a. Pop-out the first two nodes with minimum frequency from the priority queue
    min_frequency_nodes = get_nodes(min_heap, 2)

    # 4.b. Create a new node with its value (frequency) equal to the sum of the two nodes selected in Step 4. This new node will become an internal node in the Huffman Tree and the two nodes selected in Step 4 are its children (left child: lower frequency node; right child: higher frequency node)
    new_node = create_subtree(min_frequency_nodes)

    # 4.c. Reinsert the node (subtree) created in Step 5 into the priority queue
    insert_node(min_heap, new_node)

  # *** The priority queue becomes our Huffman Tree ***
  # 5. Remove the final element from the priority queue and initialize our Huffman Tree
  root = TreeNode(min_heap.heap[0].value, min_heap.heap[0].frequency, min_heap.heap[0].children[0], min_heap.heap[0].children[1])
  huffman_tree = HuffmanTree(root).root

  # 6. Build Huffman Tree
  build_huffman_tree(root)

  # Phase 2: Generate the Encoded Data
  # 7. Get Huffman code for each key in our frequencies dictionary and build our encoding table
  encoding_table = dict()
  for key, value in frequencies.items():
    huffman_code = get_huffman_code(huffman_tree, key, [])
    huffman_code = ('').join(huffman_code)
    encoding_table[key] = {
      'freq': value,
      'code': huffman_code
    }

  # 8. Encode data
  encoded_str = ""
  for c in data:
    encoded_str += encoding_table[c]['code']

  # 9. Return encoded data and Huffman Tree
  return (encoded_str, huffman_tree)

def get_frequencies(data):
  frequencies = dict()
  for c in data:
    if c in frequencies:
      frequencies[c] += 1
    else:
      frequencies[c] = 1
  return frequencies

def create_nodes(items):
  nodes = list()
  for item in items:
    node = Node(item, items[item])
    nodes.append(node)
  return nodes

def create_min_heap(nodes):
  min_heap = MinHeap(len(nodes))
  for node in nodes:
    min_heap.insert(node)
  return min_heap

def get_nodes(tree, count):
  min_nodes = list()

  while count > 0:
    node = tree.remove()
    min_nodes.append(node)
    count -= 1

  return min_nodes

def create_subtree(nodes):
  new_node = Node(None, 0)
  left_child = None
  right_child = None

  for node in nodes:
    new_node.frequency += node.frequency
    if left_child == None:
      left_child = node
    else:
      if node.frequency <= left_child.frequency:
        right_child = left_child
        left_child = node
      else:
        right_child = node

  new_node.children = [left_child, right_child]
  return new_node

def insert_node(tree, new_node):
  tree.insert(new_node)

def build_huffman_tree(node):
  if not node:
    return

  if node.left:
    left_node = TreeNode(node.left.value, node.left.frequency, node.left.children[0], node.left.children[1])
    node.left = left_node
    node.left.parent = node
    build_huffman_tree(node.left)

  if node.right:
    right_node = TreeNode(node.right.value, node.right.frequency, node.right.children[0], node.right.children[1])
    node.right = right_node
    node.right.parent = node
    build_huffman_tree(node.right)

def get_huffman_code(root, key, code):
  # Traverse through the tree searching for key. Build its Huffman Code (binary representation) as you traverse, using the bit property assigned to each branch (left, right). Return code when key is found
  if not root:
    return False

  if root.value == key:
    return True

  if root.left:
    found = get_huffman_code(root.left, key, code)
    if found:
      code.insert(0, root.left_bit)
      return code

  if root.right:
    found = get_huffman_code(root.right, key, code)
    if found:
      code.insert(0, root.right_bit)
      return code

def print_tree(root, node="root"):
  if not root:
    return

  print(node, " => ", root.value, root.frequency, root.left, root.right)

  if root.left:
    print_tree(root.left, "left")

  if root.right:
    print_tree(root.right, "right")

def huffman_decoding(data, tree):
  # 1. Initialize an empty string
  decoded_str = ""

  if len(data) == 0:
    return decoded_str

  # 2. Repeat Steps 2.a - 2.e until the encoded data is completely traversed
  i = 0
  while i < len(data):
    # 2.a. Traverse the Huffman Tree from the root
    curr = tree
    while (curr.left or curr.right):
      # 2.b. Pick a bit from the encoded data, traversing from left to right
      bit = data[i]
      # 2.c. Move left if the the bit is 0
      if bit == "0":
        curr = curr.left
      # 2.d. Move right if the bit is 1
      elif bit == "1":
        curr = curr.right
      i += 1
    # 2.e. Add the value of our leaf node to our decoded str
    decoded_str += curr.value

  # 3. Return our decoded string
  return decoded_str

if __name__ == "__main__":
  codes = {}

  # Test 1 - Repeating characters
  s = "AAAAAAABBBCCCCCCCDDEEEEEE"
  print ("\nThe size of the data is: {}".format(sys.getsizeof(s)))  # returns 74
  print ("The content of the data is: {}".format(s))  # returns "AAAAAAABBBCCCCCCCDDEEEEEE"

  encoded_data = huffman_encoding(s)
  encoded_data, tree = huffman_encoding(s)
  print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))  # returns 32
  print ("The content of the encoded data is: {}".format(encoded_data)) # returns "1010101010101000100100111111111111111000000010101010101"

  decoded_data = huffman_decoding(encoded_data, tree)
  print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data))) # returns 74
  print ("The content of the decoded data is: {}".format(decoded_data)) # returns "AAAAAAABBBCCCCCCCDDEEEEEE"

  # Test 2 - Different casing and spaces
  a_great_sentence = "The bird is the word"
  print ("\nThe size of the data is: {}".format(sys.getsizeof(a_great_sentence))) # returns 69
  print ("The content of the data is: {}".format(a_great_sentence)) # returns "The bird is the word"

  encoded_data, tree = huffman_encoding(a_great_sentence)
  print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))  # returns 36
  print ("The content of the encoded data is: {}".format(encoded_data)) # returns "1001110100111110001100101011111110000001110101110100111100010100101011"

  decoded_data = huffman_decoding(encoded_data, tree)
  print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data))) # returns 69
  print ("The content of the decoded data is: {}".format(decoded_data)) # returns "The bird is the word"

  # Test 3 - Empty input isn't encoded
  e = ""
  print ("\nThe size of the data is: {}".format(sys.getsizeof(e)))  # returns 49
  print ("The content of the data is: {}".format(e))  # returns empty string

  encoded_data, tree = huffman_encoding(e)
  print ("The encoded data has length: {} and the tree root is: {}".format(len(encoded_data), tree))  # returns 0 for length and None as tree root

  # Test 2 - Different casing, spaces and punctuation
  s2 = "It's a beautiful day outside!"
  print ("\nThe size of the data is: {}".format(sys.getsizeof(s2))) # returns 78
  print ("The content of the data is: {}".format(s2)) # returns "It's a beautiful day outside!"

  encoded_data, tree = huffman_encoding(s2)
  print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))  # returns 40
  print ("The content of the encoded data is: {}".format(encoded_data)) # returns "101110001000010011100011101010011100010100001111101100101010111001100011000111001111010000100111110110111001110"

  decoded_data = huffman_decoding(encoded_data, tree)
  print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data))) # returns 78
  print ("The content of the decoded data is: {}".format(decoded_data)) # returns "It's a beautiful day outside!"