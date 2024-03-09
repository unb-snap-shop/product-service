from flask import jsonify, make_response
from app.utils.product_catalogue import ProductCatalogue
from . import api 

product_catalogue = ProductCatalogue()  

@api.route('/products', methods=['GET'])  
def get_products():
    products = product_catalogue.list_products()
    response = make_response(jsonify(products))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
