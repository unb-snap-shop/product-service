from flask import jsonify, make_response, request, Blueprint
from app.utils.product_catalogue import ProductCatalogue
from . import api 
from app.Factory.componentManager import ComponentManager
from flask_cors import CORS


#from flask import Flask, Blueprint, request, jsonify, make_response, Response, stream_with_context, current_app

product_catalogue = ProductCatalogue()  
api = Blueprint('api', __name__)
CORS(api)

@api.route('/products', methods=['GET'])  
def get_products():
    products = product_catalogue.list_products()
    response = make_response(jsonify(products))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@api.route('/create_component', methods=['POST', 'OPTIONS'])
def create_component():
    if request.method == 'OPTIONS':
        # Respond to preflight request
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    elif request.method == 'POST':
        try:
            data = request.get_json()
            component_type = data.get('component_type')
            specifications = data.get('specifications', {})
            component = ComponentManager.create_component(component_type, specifications=specifications)
            
            response = make_response(jsonify({'message': 'Component created successfully', 'component': component}), 200)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        except Exception as e:
            return jsonify({'error': str(e)}), 500


# @api.route('/create_component', methods=['POST', 'OPTIONS'])
# def create_component():
#     if request.method == 'OPTIONS':
#         # Respond to preflight request
#         response = jsonify({'message': 'Preflight request received'})
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#         response.headers.add('Access-Control-Allow-Methods', 'POST')
#         return response
#     elif request.method == 'POST':
#         try:
#             # Extract component data from the request
#             data = request.get_json()
#             component_type = data.get('component_type')
#             specifications = data.get('specifications', {})
#             # Add more fields as needed

#             # Create the component using ComponentManager
#             component = ComponentManager.create_component(component_type, specifications=specifications)
#             response = jsonify({'message': 'Component created successfully', 'component': component})
#             response.headers.add('Access-Control-Allow-Origin', '*')
#             response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#             response.headers.add('Access-Control-Allow-Methods', 'POST')
#             return response
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500  # Return error response if an exception occurs