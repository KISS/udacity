import hashlib
from datetime import datetime

class Block:
  def __init__(self, timestamp, data, previous_hash):
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()
    self.next = None

  def calc_hash(self):
    sha = hashlib.sha256()
    base = str(self.timestamp) + self.data
    hash_str = base.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Blockchain:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert(self, data):
    if not data:
      return

    node = Block(datetime.utcnow(), data, 0)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      node.previous_hash = self.tail.hash
      self.tail.next = node
      self.tail = node

  def print(self):
    curr = self.head
    while curr:
      print("Current hash: {}, Previous hash {}".format(curr.hash, curr.previous_hash))
      curr = curr.next

# Test Case 1: Blockchain with 3 nodes
print("Test Case 1: Blockchain with 3 nodes")
blockchain_one = Blockchain()
s1 = "Random message to insert in block"
blockchain_one.insert(s1)

s2 = "Another random message to insert in block"
blockchain_one.insert(s2)

s3 = "Final message to insert in block"
blockchain_one.insert(s3)

blockchain_one.print() # prints values for 3 nodes


# Test Case 2: Blockchain with 0 nodes
print("\nTest Case 2: Blockchain with 0 nodes")
blockchain_two = Blockchain()
blockchain_two.print() # empty output


# Test Case 3: Blockchain with 1 node
print("\nTest Case 3: Blockchain with 1 node")
blockchain_three = Blockchain()

s4 = ""
blockchain_three.insert(s4) # inserting node with empty data value fails

s5 = "Single node"
blockchain_three.insert(s5)

blockchain_three.print() # prints values for 1 node