import csv

# Open the u.data file in read mode
with open('./dataset/u.data', 'r') as input_file:
    reader = csv.reader(input_file, delimiter='\t')

    # Open the u.csv file in write mode
    with open('./dataset/u.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)

        # Write the header row to the CSV file
        writer.writerow(['user_id', 'item_id', 'rating', 'timestamp'])

        # Iterate through each row in the input file and write it to the CSV file
        for row in reader:
            user_id = row[0]
            item_id = row[1]
            rating = row[2]
            timestamp = row[3]

            # Write the row to the CSV file
            writer.writerow([user_id, item_id, rating, timestamp])
