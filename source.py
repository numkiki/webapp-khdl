from flask import Flask, render_template, request, flash, redirect, url_for

import csv

app = Flask(__name__)

def read_csv(file):
    with open(file, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        products = list(reader)
    return products

products = read_csv('data/New_data_cleaned.csv')
comments = read_csv('data/final_sentiment_results.csv')

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling search queries
@app.route('/search', methods=['POST'])
def search():
    name = request.form.get('query')
    ram = request.form.get('ram')
    storage = request.form.get('storage')
    min_price = request.form.get('min_price')
    max_price = request.form.get('max_price')
    
    if not name or not min_price:
        error_message = "Please fill the name of the product and minimum price"
        return render_template('results.html', error_message=error_message)

    # Filter products based on the search criteria
    results = [product for product in products if
               (name.lower() in product['phone_name'].lower() and name.lower() != "") and
               (ram == "" or ram.lower() == product['ram'].lower()) and
               (storage == "" or storage.lower() == product['memory'].lower()) and
                (min_price == "" or float(min_price) <= float(product['price'])) and
                (max_price == "" or float(max_price) >= float(product['price']))
               ]
       
    # if results == []:
    #     error_message = "Please fill the name of the product"
    #     return render_template('results.html', error_message=error_message)
    
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)