def rearrange_digits(input_list):
  """
  Rearrange Array Elements so as to form two numbers such that their sum is maximized.

  Args:
    input_list(list): Input List
  Returns:
    (int),(int): Two maximum sums
  """
  if len(input_list) < 2:
    return input_list

  # sort list in-place
  sort(input_list, 0, len(input_list) - 1)

  # initialize output list with two empty strings
  output = ["", ""]

  # traverse list from end
  p1 = len(input_list) - 1
  p2 = len(input_list) - 2
  while p1 >= 0 or p2 >= 0:
    # add first element to first sublist in output list
    if p1 >= 0:
      output[0] = output[0] + str(input_list[p1])
      p1 -= 2
    # add second element to second sublist in output list
    if p2 >= 0:
      output[1] = output[1] + str(input_list[p2])
      p2 -= 2

  # cast strings into ints
  output[0] = int(output[0])
  output[1] = int(output[1])

  # return output list
  return output

# implementation of quick sort
def sort(arr, start, end):
  if start >= end:
    return

  pivot_index = end
  start_ptr = start

  while start_ptr < pivot_index:
    if arr[start_ptr] > arr[pivot_index]:
      # swap values
      temp = arr[pivot_index]
      arr[pivot_index] = arr[start_ptr]
      arr[start_ptr] = arr[pivot_index - 1]
      arr[pivot_index - 1] = temp
      # shift pivot to the left
      pivot_index -= 1
    else:
      start_ptr += 1

  # recursively sort the left half of our arr
  sort(arr, start, pivot_index - 1)

  # recursively sort the right half of our arr
  sort(arr, pivot_index + 1, end)

def test_function(test_case):
  output = rearrange_digits(test_case[0])
  solution = test_case[1]
  if sum(output) == sum(solution):
    print("Pass")
  else:
    print("Fail")

test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 2, 8], [84, 2]])
test_function([[9, 9], [9, 9]])
test_function([[2, 1], [1, 2]])
test_function([[1], [1]])
test_function([[], []])