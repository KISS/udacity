For this project I decided to implement the priority queue as a min-heap, using an array. The Huffman Tree is implemented as a linked list. Both the priority queue and Huffman Tree have their own node classes as well.

The huffman_encoding() method takes O(n + m + d + log(m)) time, where n is the length of data, m is the length of the min-heap, and d is the number of nodes in the Huffman Tree. log(m) represents the time it takes to perform the insert and remove operations for the min-heap. The space complexity is O(n + d + e), where n is the number of unique values in data, m is the number of nodes in the Huffman Tree, and e is the length of the encoded output string.

The huffman_decoding() method takes O(n + d) time, where n is the length of data and d is the depth of the Huffman Tree. The space complexity is O(n), where n is the length of the decoded string.

