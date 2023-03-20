import csv

input_file = './edith/final-testing-r2.csv'
output_file = './edith/final-testing-r3.csv'

with open(input_file, 'r', encoding='utf-8') as f_input, open(output_file, 'w', newline='') as f_output:
    reader = csv.DictReader(f_input)
    writer = csv.DictWriter(f_output, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        keywords = row['keywords'].split(',')
        new_keywords = []
        for keyword in keywords:
            new_keyword = "'" + keyword.strip() + "'"
            new_keywords.append(new_keyword)
        row['keywords'] = '[' + ','.join(new_keywords) + ']'
        writer.writerow(row)
