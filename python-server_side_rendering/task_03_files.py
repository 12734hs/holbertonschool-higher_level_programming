from flask import Flask, render_template, request
import parsers
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
    list_of_books = data.get('items', [])
    return render_template('items.html', list_of_books=list_of_books)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', information='Wrong source')

    if source == 'csv':
        data = parsers.parse_csv('products.csv')
        if id:
            data_with_id = 0
            for i in data:
                if str(i['id']) == str(id):
                    data_with_id = i
                    break
            return render_template('product_display.html', information=data_with_id)
        else:
            return render_template('product_display.html', information=data)

    if source == 'json':
        data = parsers.parse_json('products.json')  # это уже список
        data_with_id = None
        if id:
            for i in data:
                if str(i['id']) == str(id):
                    data_with_id = i
                    break
            return render_template('product_display.html', information=data_with_id)
        else:
            return render_template('product_display.html', information=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
