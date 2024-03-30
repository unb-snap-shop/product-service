import json

class ProductCatalogue:
    _instance = None 
    _is_initialized = False 

   
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ProductCatalogue, cls).__new__(cls)
        return cls._instance 

    def __init__(self):
        if not self._is_initialized:
            with open('app/data/products.json', 'r') as file:
                product_data = json.load(file)
                self.products = product_data.get('components', [])
            self._is_initialized = True


    def add_product(self, product):
        try:
            with open('app/data/products.json', 'r') as file:
                product_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            product_data = {'components': []}
        
        
        if 'components' not in product_data:
            product_data['components'] = []
        
        # Append the new product to the components list
        product_data['components'].append(product)
        
        with open('app/data/products.json', 'w') as file:
            json.dump(product_data, file, indent=4)

        # Update the products list
        self.products = product_data['components']


    def list_products(self):
        return self.products
