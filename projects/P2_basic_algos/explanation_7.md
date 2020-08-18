RouteTrie class:
  - insert(): The time complexity is O(n), where n is the length of paths. The space complexity is O(n), where n is the new paths that need to be created and added to the RouteTrie
  - find(): The time complexity is O(n), where n is the length of paths. The space complexity is O(1)

RouteTrieNode class:
  - insert(): The time and space complexity are O(1)

Router class:
  - add_handler(): The time and space complexity are O(n), where n is the number of paths in a path.
  - lookup():  The time and space complexity are O(n), where n is the number of paths in a path.
  - split_path(): The time complexity is O(n), where n is the number of paths in a path. The space compexity is O(n), where n is the length of the longest path added to the path_parts list.