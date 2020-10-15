import json
import matplotlib.pyplot as plt
import dateutil.parser
import datetime

file_name = "json/HKQuantityTypeIdentifierBodyMass.json"
weights_data = None

with open(file_name) as json_file:
    weights_data = json.load(json_file)


data = {}

dates = []
weights = []

for weight in weights_data:
    creationDate = weight['creationDate']
    creationDate = dateutil.parser.parse(creationDate).strftime("%m/%d/%y")
    value = int(float(weight['value']))

    # print(f"date: {creationDate} weight: {value}")

    if creationDate not in data:
        date = {
            'weights': [value],
            'numberofweights': 1,
        }
        data[creationDate] = date
    else:
        data[creationDate]["weights"].append(value)
        data[creationDate]["numberofweights"] += 1

for date in data.keys():
    item = data[date]
    total = sum(item['weights'])
    weights.append(total/item['numberofweights'])

dates = data.keys()

plt.rcParams["figure.figsize"] = (10,10)
plt.plot(dates, weights)
plt.xlabel("Dates")
plt.xticks(rotation=90)
plt.ylabel("Weights")

plt.show()
