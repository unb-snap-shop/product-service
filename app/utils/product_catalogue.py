import json

class ProductCatalogue:
    _instance = None # _instance holds the single instance of ProductCatalogue, initially None
    _is_initialized = False 

    # Override new to check if an instance already exists
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ProductCatalogue, cls).__new__(cls)
        return cls._instance # else Return the instance that already exists

    def __init__(self):
        if not self._is_initialized:
            with open('app/data/products.json', 'r') as file:
                product_data = json.load(file)
                self.products = product_data.get('components', [])
            self._is_initialized = True

    # def create_component(self, component_data):
    #     #Factory method to create components based on component_data
    #     type = component_data.get('type')
    #     if not type:
    #         raise ValueError("Component data must contain a 'type' field.")

        
    #     for product in self.products:
    #         if product['type'] == type:
    #             return product  
    #     raise ValueError(f"No product found for component type: {type}")


    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        return self.products
