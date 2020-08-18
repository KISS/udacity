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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
# store unique numbers in a set
unique_numbers = set()

# iterate through texts
for text in texts:
    sending_number = text[0]
    receiving_number = text[1]

    # if incoming number not in set, add it
    unique_numbers.add(sending_number)

    # if outgoing number not in set, add it
    unique_numbers.add(receiving_number)

# iterate through calls
for call in calls:
    calling_number = call[0]
    receiving_number = call[1]

    # if incoming number not in set, add it
    unique_numbers.add(calling_number)

    # if outgoing number not in set, add it
    unique_numbers.add(receiving_number)

print("There are %s different telephone numbers in the records." % len(unique_numbers))