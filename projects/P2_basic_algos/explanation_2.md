For this problem I used a variation of binary search to locate the pivot point, and binary search to find the target number in either subarray.

rotated_array_search():
  - The time complexity is O(log(n))
  - The space complexity is O(1), if not accounting for the stack memory taken up by the use of recursion.

find_pivot():
  - The time complexity is O(log(n))
  - The space complexity is O(1)

binary_search():
  - The time complexity is O(log(n))
  - The space complexity is O(1)