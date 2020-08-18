class Node(object):
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None

class DoublyLinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

class LRU_Cache(object):
  def __init__(self, capacity):
    # Initialize class variables
    self.cache = dict()
    self.capacity = capacity
    self.LRU = DoublyLinkedList()

  def get(self, key):
    # Retrieve item from provided key. Return -1 if nonexistent.
    if key in self.cache:
      self.refresh_LRU_entry(key)
      return self.cache[key]
    else:
      return -1

  def set(self, key, value):
    # Edge case where LRU is initialized with a capacity of 0 less.
    if self.capacity <= 0:
      return

    # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
    if key not in self.cache:
        if self.is_full():
          self.remove_LRU_entry()
        # add new entry
        self.cache[key] = value
        self.add_to_LRU(key)

  def is_full(self):
    # check if cache is at capacity
    return len(self.cache) == self.capacity

  def add_to_LRU(self, key):
    node = Node(key)
    # if our LRU isn't empty, add our new node to the end
    if self.LRU.tail:
      node.prev = self.LRU.tail
      self.LRU.tail.next = node
      self.LRU.tail = node
    else:
      # if our LRU is empty, set our new node as the head and tail
      self.LRU.head = node
      self.LRU.tail = node

  def remove_LRU_entry(self):
    if self.LRU.head:
      # delete the head since this is the LRU entry
      node_to_remove = self.LRU.head
      self.LRU.head = self.LRU.head.next
      # if we didn't empty our LRU, update the head's prev pointer
      if self.LRU.head:
        self.LRU.head.prev = None
      # delete LRU key from our cache
      del self.cache[node_to_remove.val]

  def refresh_LRU_entry(self, key):
    if self.LRU.head:
      # if key is our head, update our head and tail pointers
      if self.LRU.head.val == key:
        # if we only have one node in our list, set head and tail to None
        if self.LRU.head == self.LRU.tail:
          self.LRU.head = None
          self.LRU.tail = None
        else:
          # shift head to next node and set our target entry as our new tail
          node_to_update = self.LRU.head
          self.LRU.head = self.LRU.head.next
          self.LRU.head.prev = None
          # add node to end of list
          self.LRU.tail.next = node_to_update
          node_to_update.prev = self.LRU.tail
          node_to_update.next = None
          self.LRU.tail = node_to_update
      # if key is not our head nor our tail, search for it in our list and set it as our new tail
      elif self.LRU.tail.val != key:
        # start at the 2nd node in our list
        curr = self.LRU.head.next
        prev = curr.prev
        # exit if curr.next is our tail since we know our key isn't at the tail
        while curr.next and curr.next != self.LRU.tail:
          if curr.val == key:
            # remove curr from its current position
            prev.next = curr.next
            curr.next.prev = prev
            # move curr to tail
            curr.prev = self.LRU.tail
            curr.next = None
            self.LRU.tail.next = curr
            self.LRU.tail = curr
            break
          else:
            prev = curr
            curr = curr.next

  def print_LRU(self):
    curr = self.LRU.head
    while curr:
      print(curr.val)
      curr = curr.next

# Test Case 1: Cache Capacity 5
cache_one = LRU_Cache(5)

print("get(1): ", cache_one.get(1))      # returns -1 because 1 is not present in the cache, the cache is empty

cache_one.set(3, 3)
cache_one.set(1, 1)
cache_one.set(2, 2)
cache_one.set(4, 4)

print("get(1): ", cache_one.get(1))      # returns 1
print("get(2): ", cache_one.get(2))      # returns 2
print("get(9): ", cache_one.get(9))      # returns -1 because 9 is not present in the cache

cache_one.set(5, 5)
cache_one.set(6, 6)

print("get(3): ", cache_one.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# Test Case 2: Cache Capacity 0
cache_two = LRU_Cache(0)
cache_two.set(1, 1)
print("get(1): ", cache_two.get(1))      # returns -1 because cache capacity is 0


# Test Case 3: Cache Capacity 1
cache_three = LRU_Cache(1)
cache_three.set(1, 1)
cache_three.set(3, 3)

print("get(1): ", cache_three.get(1))    # returns -1 because 1 was removed to make room for 3
print("get(3): ", cache_three.get(3))    # returns 3