import random

class ComponentFactory:
    registry = {}
    component_id_counter = 1  # Initialize a counter

    @classmethod
    def register_component(cls, component_type, constructor):
        cls.registry[component_type] = constructor
         
    @classmethod
    def create_component(cls, component_type, component_data):
        if component_type in cls.registry:
            constructor = cls.registry[component_type]
            component_data["id"] = cls.generate_random_id()  # Generate a random ID
            return constructor(**component_data)
        else:
            raise ValueError(f"Component type {component_type} not registered")
    
    @classmethod
    def generate_random_id(cls):
        return random.randint(1, 1000000)  # Adjust the range as needed
