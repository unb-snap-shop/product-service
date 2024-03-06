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
            with open(data.products.json, 'r') as file:
                data = json.load(file)
                self.products = data.get('components', [])
            self._is_initialized = True


    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        return self.products
