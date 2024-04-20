import csv

def read_csv():
    with open('data/data_cleaned.csv', 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        products = list(reader)
    return products

a = read_csv()

for product in a:
    print(product['Link'])
