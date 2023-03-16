# load the data from csvimport csv

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]
