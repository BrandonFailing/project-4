# load the data from csv
import csv

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]
