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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# create set for tracking potential telemarketers
potential_telemarketers = set()

# iterate through calls and add calling number to telemarketer set
for call in calls:
    potential_telemarketers.add(call[0])

# iterate through calls and remove receiving number from telemarketer set
for call in calls:
    receiving_number = call[1]

    if receiving_number in potential_telemarketers:
        potential_telemarketers.remove(receiving_number)

# iterate through texts and remove sending and receiving number from telemarketer set
for text in texts:
    sending_number = text[0]
    receiving_number = text[1]

    if sending_number in potential_telemarketers:
        potential_telemarketers.remove(sending_number)

    if receiving_number in potential_telemarketers:
        potential_telemarketers.remove(receiving_number)

# create array with final phone numbers, sort, and print
output = []
for number in potential_telemarketers:
    output.append(number)

print("These numbers could be telemarketers: ")
for n in sorted(output):
    print(n)