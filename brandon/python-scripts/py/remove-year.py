import csv
import re

input_file = './data/u-movie-list.csv'
output_file = './data/u-movie-list-year-removed.csv'

with open(input_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    rows = []
    for row in reader:
        name = row[0]
        # Remove parentheses and text between them
        name = re.sub(r'\(.*\)', '', name)
        row[0] = name.strip()
        rows.append(row)

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)
