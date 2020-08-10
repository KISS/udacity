For this problem I used a Linked List to implement the Blockchain, and used the timestamp and data properties of a block to create its hash.

The runtime for inserting a new block into the Blockchain is O(n) time and O(n + c) space, where n is the space the block itself takes up and c is the time it takes to create the new hash.