import csv

def filter_csv(input_file, output_file, conditions):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        filtered_rows = [row for row in reader if all(eval(f"row['{col}']{op}{repr(val)}") for col, op, val in conditions)]
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=filtered_rows[0].keys())
        writer.writeheader()
        writer.writerows(filtered_rows)

conditions = [
    ('Age', '>=', 25),
    ('Country', '==', 'UK')
]

filter_csv('input.csv', 'output.csv', conditions)
