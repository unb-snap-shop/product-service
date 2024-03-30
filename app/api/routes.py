from flask import jsonify, make_response, request, Blueprint
from app.utils.product_catalogue import ProductCatalogue
from app.factory.component_manager import ComponentManager
from flask_cors import CORS

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
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    elif request.method == 'POST':
        try:
            data = request.get_json()
            print(data)
            component_type = data.get('type')
            print(component_type)

            data.pop('type')
            component = ComponentManager.create_component(component_type, **data)

            response = make_response(jsonify({'message': 'Component created successfully', 'component': component}),
                                     200)
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Methods', 'POST')
            return response

        except Exception as e:
            print(e)
            return jsonify({'error': str(e)}), 500
