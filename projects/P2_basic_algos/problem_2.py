def rotated_array_search(input_list, number):
  """
  Find the index by searching in a rotated sorted array

  Args:
    input_list(array), number(int): Input array to search and the target
  Returns:
    int: Index or -1
  """
  if not input_list:
    return -1

  # find pivot point
  pivot = find_pivot(input_list, 0, len(input_list) - 1)

  # case where pivot = -1 (aka array is sorted)
  if pivot == -1:
    return binary_search(input_list, number, 0, len(input_list) - 1)

  # case where value at pivot index is value we're searching for
  if input_list[pivot] == number:
    return pivot

  # check which subarray our number might be in and run binary search on subarray
  if number >= input_list[0]:
    # traverse the left half
    return binary_search(input_list, number, 0, pivot - 1)
  else:
    # traverse the right half
    return binary_search(input_list, number, pivot + 1, len(input_list) - 1)

def find_pivot(arr, start, end):
  if start > end:
    return -1

  mid = (start + end) // 2

  # if the value at arr[mid] is greater than the value to its right, we're at our pivot
  if arr[mid] > arr[mid + 1]:
    return mid
  elif arr[start] >= arr[mid]:
    # traverse left half of array
    return find_pivot(arr, start, mid - 1)
  else:
    # traverse right half of array
    return find_pivot(arr, mid + 1, end)

def binary_search(arr, target, start, end):
  if start > end:
    return -1

  mid = (start + end) // 2

  if arr[mid] == target:
    return mid
  elif arr[mid] < target:
    return binary_search(arr, target, mid + 1, end)
  else:
    return binary_search(arr, target, start, mid - 1)

def linear_search(input_list, number):
  for index, element in enumerate(input_list):
    if element == number:
      return index
  return -1

def test_function(test_case):
  input_list = test_case[0]
  number = test_case[1]
  if linear_search(input_list, number) == rotated_array_search(input_list, number):
    print("Pass")
  else:
    print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

a1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
print(rotated_array_search(a1, 1))    # returns 6
print(rotated_array_search(a1, 10))   # returns 5

a2 = [30, 40, 50, 10, 20]
print(rotated_array_search(a2, 20))   # returns 4
print(rotated_array_search(a2, 30))   # returns 0

a3 = [2, 3, 4, 5, 6, 1]
print(rotated_array_search(a3, 3))    # returns 1

a4 = []
print(rotated_array_search(a4, 0))    # returns -1