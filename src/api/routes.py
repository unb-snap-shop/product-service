from flask import Flask, jsonify
from product_catalogue import ProductCatalogue

app = Flask(__name__)

product_catalogue = ProductCatalogue('./data/products.json')

@app.route('/api/products', methods=['GET'])
def get_products():
    products = product_catalogue.list_products()
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)
