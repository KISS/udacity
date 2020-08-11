For this problem I used a variation of binary search to location the pivot point, and binary search to find the target number in either subarray.

The time complexity for rotated_array_search() is O(log(n)) and the space complexity is O(1), if not accounting for the stack memory taken up by the use of recursion.