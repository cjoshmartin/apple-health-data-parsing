import json
import matplotlib.pyplot as plt
import dateutil.parser
import datetime

file_name = "json/HKQuantityTypeIdentifierBodyFatPercentage.json"
_data = None

with open(file_name) as json_file:
    _data = json.load(json_file)


data_set = {}

for fat_percentage in _data:
    creationDate = fat_percentage['creationDate']
    creationDate = dateutil.parser.parse(creationDate).strftime("%m/%d/%y")
    value = float(fat_percentage['value']) * 100


    if creationDate not in _data:
        date = {
            'datepoint': [value],
            'values': 1,
        }
        data_set[creationDate] = date
    else:
        data_set[creationDate]["datepoint"].append(value)
        data_set[creationDate]["values"] += 1

dates = data_set.keys()
fat_percentages = []

for date in dates:
    item = data_set[date]
    avg = sum(item["datepoint"])/ item["values"]
    fat_percentages.append(avg)


plt.rcParams["figure.figsize"] = (10,10)
plt.plot(dates, fat_percentages)
plt.xlabel("Dates")
plt.xticks(rotation=90)
plt.ylabel("fat Percentages (in %)")

plt.show()

