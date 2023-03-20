import csv

# Define the index of the column to remove leading spaces from
column_index = 1  # replace with the index of the desired column

# Read the data from the input CSV file
with open('movie-list-r1.csv', 'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# Remove leading spaces from values in the specified column
for row in data:
    row[column_index] = row[column_index].lstrip()

# Write the updated data to a new CSV file
with open('movie-list-r2.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
