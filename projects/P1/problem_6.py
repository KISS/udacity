class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __repr__(self):
    return str(self.value)

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __str__(self):
    cur_head = self.head
    out_string = ""
    while cur_head:
      out_string += str(cur_head.value) + " -> "
      cur_head = cur_head.next
    return out_string

  def append(self, value):
    node = Node(value)
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node

  def size(self):
    size = 0
    node = self.head
    while node:
      size += 1
      node = node.next
    return size

def union(llist_1, llist_2):
  # initalize output list and append dummy node
  output_list = LinkedList()
  output_list.append(Node(-1))

  # initialize a set to track seen values
  seen = set()

  # iterate through llist_1, add unseen values to output list
  curr = llist_1.head
  while curr:
    if curr.value not in seen:
      seen.add(curr.value)
      new_node = Node(curr.value)
      output_list.append(new_node)
    curr = curr.next

  # iterate through llist_2, add unseen values to output list
  curr = llist_2.head
  while curr:
    if curr.value not in seen:
      seen.add(curr.value)
      new_node = Node(curr.value)
      output_list.append(new_node)
    curr = curr.next

  output_list.head = output_list.head.next
  return output_list

def intersection(llist_1, llist_2):
  # initialize a set to track values in llist_1
  llist_1_values = set()

  # iterate through llist_1 adding values to set
  curr = llist_1.head
  while curr:
    if curr.value not in llist_1_values:
      llist_1_values.add(curr.value)
    curr = curr.next

  # initialize output list and append dummy node
  output_list = LinkedList()
  output_list.append(Node(-1))

  # initialize a set to track nodes that should be in our output list
  output_values = set()

  # iterate through llist_2, add nodes to output list that meet criteria
  curr = llist_2.head
  while curr:
    # if curr.value exists in llist_1 and hasn't been added to our output, create a
    # new node for curr.value and add it to our output list
    if curr.value in llist_1_values and curr.value not in output_values:
      output_values.add(curr.value)
      new_node = Node(curr.value)
      output_list.append(new_node)
    curr = curr.next

  output_list.head = output_list.head.next
  return output_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
  linked_list_1.append(i)

for i in element_2:
  linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))        # returns a list containing {32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21}
print (intersection(linked_list_1,linked_list_2)) # returns a list containing {6, 4, 21}


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
  linked_list_3.append(i)

for i in element_2:
  linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))        # returns a list containing {65, 2, 35, 3, 4, 6, 1, 7, 8, 9, 11, 21, 23}
print (intersection(linked_list_3,linked_list_4)) # returns an empty list


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3, 3]
element_2 = []

for i in element_1:
  linked_list_5.append(i)

for i in element_2:
  linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))        # returns a list containing {3}
print (intersection(linked_list_5,linked_list_6)) # returns an empty list


# Test case 4

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
  linked_list_5.append(i)

for i in element_2:
  linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))        # returns an empty list
print (intersection(linked_list_5,linked_list_6)) # returns an empty list