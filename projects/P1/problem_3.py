import sys

class Node(object):
  def __init__(self, value, frequency=1):
    self.value = value
    self.frequency = frequency
    self.left = None
    self.right = None

# binary tree: implemented using an array
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

    # while we haven't reached our root node and our child node frequency is of a smaller
    # value than our parent frequency, swap the parent and child values and move up our tree
    while child_index > 0 and self.heap[child_index].frequency < self.heap[parent_index].frequency:
      # extra value and frequency parameters from node
      child_values = (self.heap[child_index].value, self.heap[child_index].frequency)
      parent_values = (self.heap[parent_index].value, self.heap[parent_index].frequency)

      # swap parent and child value and frequency parameters, to ensure the smallest frequency is the parent
      self.heap[parent_index].value = child_values[0]
      self.heap[parent_index].frequency = child_values[1]
      self.heap[child_index].value = parent_values[0]
      self.heap[child_index].frequency = parent_values[1]

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
    node_to_remove = self.heap[0]
    # move last element values to root
    self.heap[0].value = self.heap[self.next_index - 1].value
    self.heap[0].frequency = self.heap[self.next_index -1].frequency
    # reset last element to None
    self.heap[self.next_index - 1] = None
    # decrement next_index
    self.next_index -= 1

    # down-heapify as needed
    parent_index = 0

    # explore the heap while we still have values to visit
    while parent_index < self.next_index:
      parent_values = (self.heap[parent_index].value, self.heap[parent_index].frequency)
      new_values = None

      left_child_index = 2 * parent_index + 1
      right_child_index = 2 * parent_index + 2

      # check left child
      if self.heap[left_child_index]:
        new_values = (self.heap[left_child_index].value, self.heap[left_child_index].frequency)

      # check right child
      if self.heap[right_child_index]:
        min_freq = min(new_values[1], self.heap[right_child_index].frequency)
        if min_freq != new_values[1]:
          new_values = (self.heap[right_child_index].value, self.heap[right_child_index].frequency)

      # if our new_values are different from our current parent values, verify
      # which child node needs to be switched with our parent, do the switch,
      # and update our parent index to the child index for the node we switched
      # with to continue our down-heapify.
      if new_values and parent_values[1] > new_values[1]:
        self.heap[parent_index].value = new_values[0]
        self.heap[parent_index].frequency = new_values[1]

        # if our new_values came from our left child, update our left child
        if self.heap[left_child_index] and self.heap[left_child_index].value == new_values[0] and self.heap[left_child_index].frequency == new_values[1]:
          self.heap[left_child_index].value = parent_values[0]
          self.heap[left_child_index].frequency = parent_values[1]
          parent_index = left_child_index
        else:
          # our new_values came from our right child, so update our right child
          self.heap[right_child_index].value = parent_values[0]
          self.heap[right_child_index].frequency = parent_values[1]
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
  # Phase 1: Build the Huffman Tree
    # 1. Determine the frequency of each character in the message
    frequencies = get_frequencies(data)

    # 2. Create a node for each character containing: value, frequency, left child, right child
    nodes = create_nodes(frequencies)

    # TODO: remove - just for testing
    # for node in nodes:
    #   print(node.value, node.frequency)
    # return

    # 3. Create a priority queue containing each node (character) - implement this as a min-heap, sorted based on the frequency of each node
    min_heap = create_min_heap(nodes)

    # REPEAT Steps 4 - 6 until there is only 1 element left in the priorty queue
    while min_heap.heap[0] and min_heap.heap[1] != None:
      # 4. Pop-out the first two nodes with minimum frequency from the priority queue
      min_frequency_nodes = get_nodes(min_heap, 2)

      # 5. Create a new node with its value (frequency) equal to the sum of the two nodes selected in Step 4. This new node will become an internal node in the Huffman Tree and the two nodes selected in Step 4 are its children (left child: lower frequency node; right child: higher frequency node)
      new_node = create_subtree(min_frequency_nodes)

      # 6. Reinsert the node (subtree) created in Step 5 into the priority queue
      insert_node(min_heap, new_node)

    # *** The priority queue becomes our Huffman Tree ***
    # 8. Remove the final element from the priority queue, initializing our Huffman Tree
    huffman_tree = get_nodes(min_heap, 1)[0]
    # TODO: remove - just for testing
    # print("Our Huffman Tree")
    # print(huffman_tree.value, huffman_tree.frequency)
    # print(huffman_tree.left.value, huffman_tree.right.value)

    # 9. Traverse through the tree, set the value of each node: 0 for the left child; 1 for the right child
    update_huffman_tree(huffman_tree)
    # TODO: remove - just for testing
    # print("Our Huffman Tree -- Updated")
    # print(huffman_tree.value, huffman_tree.frequency)
    # print(huffman_tree.left.value, huffman_tree.right.value)

  # Phase 2: Generate the Encoded Data
    # 10. Traverse through the tree exploring each leaf node and generating its Huffman Code (binary representation) as you traverse, using the bit property assigned to each branch (left, right)
    pass

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
  # Initialize min-heap
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
      if node.frequency < left_child.frequency:
        right_child = left_child
        left_child = node
      else:
        right_child = node

  new_node.left = left_child
  new_node.right = right_child
  return new_node

def insert_node(tree, new_node):
  tree.insert(new_node)

def update_huffman_tree(root):
    if not root:
      return

    curr = root

    if curr.left:
      curr.left.value = 0
      update_huffman_tree(curr.left)

    if curr.right:
      curr.right.value = 1
      update_huffman_tree(curr.right)


def huffman_decoding(data, tree):
  # 1. Initialize an empty string
  # 2. Pick a bit from the encoded data, traversing from left to right
  # 3. Traverse the Huffman Tree from the root
        # 3.a. Move left if the the bit is 0
        # 3.b. Move right if the bit is 1
  # 4. Repeat Steps 2 - 3 until the encoded data is completely traversed
  pass

if __name__ == "__main__":
  codes = {}

  a_great_sentence = "The bird is the word"

  print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
  print ("The content of the data is: {}\n".format(a_great_sentence))

  encoded_data = huffman_encoding(a_great_sentence)
  # encoded_data, tree = huffman_encoding(a_great_sentence)

  # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
  # print ("The content of the encoded data is: {}\n".format(encoded_data))

  # decoded_data = huffman_decoding(encoded_data, tree)

  # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
  # print ("The content of the encoded data is: {}\n".format(decoded_data))