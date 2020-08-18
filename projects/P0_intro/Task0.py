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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
text = texts[0]
print("First record of texts, {0} texts {1} at time {2}".format(text[0], text[1], text[2]))

call = calls[-1]
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(call[0], call[1], call[2], call[3]))