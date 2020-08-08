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

blockchain = Blockchain()
s1 = "Random message to insert in block"
blockchain.insert(s1)

s2 = "Another random message to insert in block"
blockchain.insert(s2)

s3 = "Final message to insert in block"
blockchain.insert(s3)

s4 = ""
blockchain.insert(s4)

blockchain.print() # prints values for 3 nodes