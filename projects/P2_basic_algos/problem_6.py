def get_min_max(ints):
  """
  Return a tuple(min, max) out of list of unsorted integers.

  Args:
    ints(list): list of integers containing one or more integers
  """
  # if empty input, return None
  if not ints:
    return

  # initialize variables to track min and max values to the first value in input
  min_val = ints[0]
  max_val = ints[0]

  # iterate through array, starting at the second value
  for i in range(1, len(ints)):
    if ints[i] < min_val:
      min_val = ints[i]

    if ints[i] > max_val:
      max_val = ints[i]

  # return min,max tuple
  return (min_val, max_val)

arr1 = [9, 1, 2, 3, 3, 6, 7, 8, 5, 0]
print ("Pass" if ((0, 9) == get_min_max(arr1)) else "Fail")

arr2 = [5, 6, 1, 2, 0, -1, 5, 200]
print ("Pass" if ((-1, 200) == get_min_max(arr2)) else "Fail")

arr3 = []
print ("Pass" if (None == get_min_max(arr3)) else "Fail")

arr4 = [2]
print ("Pass" if ((2, 2) == get_min_max(arr4)) else "Fail")