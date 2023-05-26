import csv
from sys import argv
import decisiontree as dt

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

examples = read_csv(argv[1])

# Extract attribute names from the column headers
attributes = list(examples[0].keys())[1:-1]

# Extract target attribute name
target_attribute = list(examples[0].keys())[-1]

tree = dt.ID3(examples, attributes, target_attribute)