"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
# create a dictionary to track phone numbers
# and their time spent on a call: {phone_num: time_on_calls}
time_on_calls = {}

# iterate through all calls
for call in calls:
    calling_number = call[0]
    receiving_number = call[1]
    duration = int(call[3])

    # if calling number exists in dict, increment call time
    # else, add calling number to dict and set time to call duration
    if calling_number in time_on_calls:
        time_on_calls[calling_number] += duration
    else:
        time_on_calls[calling_number] = duration

    # if receiving number exists in dict, increment call time
    # else, add receiving number to dict and set time to call duration
    if receiving_number in time_on_calls:
        time_on_calls[receiving_number] += duration
    else:
        time_on_calls[receiving_number] = duration

# create variables to track current max time and associate number
max_time_so_far = -1
phone_number = None

# iterate through each caller in dict, if their call time totals are
# greater than the current max_duration, update max_duration and caller
for number, time in time_on_calls.items():
    if time > max_time_so_far:
        max_time_so_far = time
        phone_number = number

print(f"{phone_number} spent the longest time, {max_time_so_far} seconds, on the phone during September 2016.")