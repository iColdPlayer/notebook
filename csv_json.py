import os
import csv, json
"""
CSV to JSON
"""
csv_path = open('data/villages.csv', 'r')

data_json = open("data/json/villages.json", 'w')

# dumping
field_names = ("id_row", "id_villages", "village_name")
reader = csv.DictReader( csv_path, field_names)
for row in reader:
    json.dump(row, data_json)
    data_json.write('\n')

