import xml.etree.ElementTree as ET
import json

print("Starting to parse apple health data...")

print("Reading Apple Health data into RAM...")
data = {}
root = ET.parse("export.xml").getroot()

print("Done Reading data into RAM...")

print("Starting to parsing data now...")
for type_tag in root.findall("Record"):
    type_of_record = type_tag.get("type")
    new_record = type_tag.attrib

    if type_of_record not in data:
        data[type_of_record] =[new_record]
    else:
        data[type_of_record].append(new_record)


print("Finished parsing data...")
print("writting data to json files")

for type_of_record in data:
    file_name = f"json/{type_of_record}.json"
    print(f"writing the {file_name} to disk....")

    with open(file_name, "w") as outfile:
        json.dump(data[type_of_record], indent=4, fp=outfile)

print("Done...")
