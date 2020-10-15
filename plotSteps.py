import json
import matplotlib.pyplot as plt
import dateutil.parser
import datetime
import sys

file_name = "json/HKQuantityTypeIdentifierStepCount.json"
_data = None

with open(file_name) as json_file:
    _data = json.load(json_file)


data_set = {}

toolbar_width = len(_data)
# setup toolbar

for i, entry in enumerate(_data):
    creationDate = entry['creationDate']
    creationDate = dateutil.parser.parse(creationDate).strftime("%m/%d/%y")
    value = int(entry['value'])


    if creationDate not in _data:
        date = {
            'datepoint': [value],
        }
        data_set[creationDate] = date
    else:
        data_set[creationDate]["datepoint"].append(value)
    
    progress = ((i+1)/toolbar_width) * 100
    sys.stdout.write(f"\r current precentage: {round(progress, 2)}% ({i}/{toolbar_width})")
    sys.stdout.flush()


dates = data_set.keys()
steps = []

for date in dates:
    item = data_set[date]
    total = sum(item["datepoint"])
    steps.append(total)


plt.rcParams["figure.figsize"] = (10,10)
plt.plot(dates, steps)
plt.xlabel("Dates")
plt.xticks(rotation=90)
plt.ylabel("Steps")

plt.show()

