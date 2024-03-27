import json
import random
from concreteFactory import CPUFactory, GPUFactory, MotherboardFactory, RAMFactory, StorageFactory

class ComponentManager:
    factory_registry = {
        'CPU': CPUFactory(),
        'GPU': GPUFactory(),
        'Motherboard': MotherboardFactory(),
        'RAM': RAMFactory(),
        'Storage': StorageFactory()
    }

    @staticmethod
    def create_component(component_type, **data):
        if component_type in ComponentManager.factory_registry:
            factory = ComponentManager.factory_registry[component_type]
            data["id"] = ComponentManager.generate_random_id()
            component = factory.create_component(**data)
            ComponentManager._write_to_json(component)
            return component
        else:
            raise ValueError(f"Component type {component_type} not registered")

    @staticmethod
    def generate_random_id():
        return random.randint(1, 1000000)

    @staticmethod
    def _write_to_json(component):
        # Convert the component object to a dictionary, assuming it has a method to do so
        # or define the conversion logic here if not.
        product_data = {
            'id': component.id,
            'type': component.type,
            'brand': component.brand,
            'model': component.model,
            'specifications': component.specifications,
            'price': component.price
        }
        file_path = 'testproducts.json'
        # Read the current data in the JSON file
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        
        # Append new product data
        data.append(product_data)
        
        # Write the updated data back to the JSON file
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
