# Read the data from the input file and remove quotes
with open('movie-list.txt', 'r') as infile:
    data = infile.read().replace("'", "").replace('"', '')

# Write the updated data to a new file
with open('movie-list-r1.txt', 'w') as outfile:
    outfile.write(data)
