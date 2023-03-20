import csv

input_file = './edith/final-testing.csv'
output_file = './edith/final-testing-r1.csv'

with open(input_file, 'r', encoding='utf-8') as f_input, open(output_file, 'w', newline='') as f_output:
    reader = csv.DictReader(f_input)
    writer = csv.DictWriter(f_output, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        genres = row['genrestring'].split(',')
        new_genres = []
        for genre in genres:
            new_genre = "'" + genre.strip() + "'"
            new_genres.append(new_genre)
        row['genrestring'] = '[' + ','.join(new_genres) + ']'
        writer.writerow(row)
