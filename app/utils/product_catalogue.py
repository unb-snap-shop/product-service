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
    # Attempt to open the existing JSON file
        try:
            with open('app/data/products.json', 'r') as file:
                # Load the JSON data from the file
                product_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or contains invalid JSON,
            # initialize product_data with an empty 'components' list
            product_data = {'components': []}
        
        # Check if 'components' key exists, and if not, initialize it as an empty list
        if 'components' not in product_data:
            product_data['components'] = []
        
        # Append the new product to the 'components' list
        product_data['components'].append(product)
        
        # Overwrite the JSON file with the updated product data
        with open('app/data/products.json', 'w') as file:
            json.dump(product_data, file, indent=4)

        # Update the in-memory products list
        self.products = product_data['components']


    def list_products(self):
        return self.products
