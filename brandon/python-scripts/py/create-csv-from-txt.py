import csv

# Read the comma-separated values from the text file
with open('movie-list-r1.txt', 'r') as f:
    data = [line.strip().split(',') for line in f]

# Create a new list of rows with the "movie-names" column
rows = [["movie-names"] + row for row in data]

# Write the data to a new CSV file
with open('movie-list.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
