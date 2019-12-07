import os
import csv
import xml
import json


# this is the csv source file that we want to convert to our json data.
csv_sumber = open("/home/icoldplayer/Documents/python/learning/data/districts.csv", 'r')


# the destination that we create after we convert the csv file itself.
data_json = open("/home/icoldplayer/Documents/python/learning/data/districts.json", 'w')


# for dumping
field_names = ("IDNumber","Message")
reader = csv.DictReader( csv_sumber, field_names)
for row in reader:
    json.dump(row, data_json)
    data_json.write('\n')

