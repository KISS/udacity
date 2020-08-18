def sqrt(number):
  """
  Calculate the floored square root of a number

  Args:
    number(int): Number to find the floored squared root
  Returns:
    int: Floored Square Root
  """
  if number < 0:
    return "ValueError: Number must be positive"

  start = 1
  end = number

  while start <= end:
    mid = (start + end) // 2
    num = mid * mid

    if num == number:
      # mid is the sqrt of our input
      return mid
    elif num < number:
      # shift our start to mid + 1
      start = mid + 1
    else:
      # shift our end to mid - 1
      end = mid - 1

  # return end because its our floor (mid - 1)
  return end

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print(sqrt(-27))  # prints ValueError: Number must be positive