import os
import glob
import csv
from xlsxwriter.workbook import Workbook

for csv_file in glob.glob(os.path.join('.', 'data/*.csv')):
    workbook = Workbook(csv_file[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csv_file, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
                print("converting...")
    workbook.close()