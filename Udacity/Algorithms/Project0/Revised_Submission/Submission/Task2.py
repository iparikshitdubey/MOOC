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

dict_duration = {}  # creating a dictionary
for call in calls:
    if call[0] not in dict_duration.keys():
        dict_duration[call[0]] = int(call[-1])
    else:
        dict_duration[call[0]] += int(call[-1])

    if call[1] not in dict_duration.keys():
        dict_duration[call[1]] = int(call[-1])
    else:
        dict_duration[call[1]] += int(call[-1])

max_duration = None
phone_number = None

for key in dict_duration.keys():
    if max_duration == None or max_duration < dict_duration[key]:
        max_duration = dict_duration[key]
        phone_number = key

print(str(phone_number) + " spent the longest time, " + str(max_duration) + " seconds, on the phone during September 2016.")