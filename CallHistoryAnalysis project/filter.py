import csv

def filter_call_history(input_file, output_file, filter_names):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for row in reader:
            for i in filter_names:
                if i.lower() in row['name'].lower():
                    writer.writerow(row)

# Example usage:
input_file = 'h1.csv'  # Replace with your input CSV file
output_file = 'filtered_call_history.csv'  # Output CSV file with filtered records
filter_names = ['Chandrashekar Vnr', 'Hemanth Vnr', 'Tilak VNR', 'Chandu Vnr', 'Raghava Vnr']

filter_call_history(input_file, output_file, filter_names)
