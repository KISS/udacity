"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# initialize variable with Bangalore prefix
bangalore_prefix = "(080)"

# initialize variables needed to track mobile numbers
mobile_prefix = {"7", "8", "9"}
mobile_code_len = 4

# track unique codes for receiving numbers
unique_codes = set()

# track calls made from Bangalore to local numbers
calls_from_bangalore = 0
outgoing_local_calls = 0

# iterate through calls
for call in calls:
  calling_number = call[0]

  # if calling number contains the Bangalore prefix extract the area code or mobile prefix of the receiving phone number and store in set
  if calling_number.startswith(bangalore_prefix):
    prefix_to_add = ""
    receiving_number = call[1]
    calls_from_bangalore += 1

    # case where receiving number is local
    if receiving_number.startswith(bangalore_prefix):
      outgoing_local_calls += 1

    # case where receiving number is a fixed line
    if receiving_number[0] == "(" and receiving_number[1] == "0":
      visit_next_char = True
      i = 0
      while visit_next_char and receiving_number:
        c = receiving_number[i]
        if c == ")":
          visit_next_char = False
        prefix_to_add += c
        i += 1

    # case where receiving number is a mobile number
    if receiving_number[0] in mobile_prefix:
      i = 0
      while i < mobile_code_len:
        prefix_to_add += receiving_number[i]
        i += 1

    if prefix_to_add:
      unique_codes.add(prefix_to_add)

# create array to enable sorting of unique codes
output = []
for n in unique_codes:
  output.append(n)

### Part A ####
print("The numbers called by people in Bangalore have codes:")
for n in sorted(output):
  print(n)

### Part B ####
percentage_local_calls = round((outgoing_local_calls/calls_from_bangalore) * 100, 2)

print(f"{percentage_local_calls} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")