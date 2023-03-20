import csv

# Read the data from the input CSV file
with open('movie-list.csv', 'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# Transpose the data to convert columns to rows
transposed = list(map(list, zip(*data)))

# Write the transposed data to a new CSV file
with open('movie-list-r1.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(transposed)
