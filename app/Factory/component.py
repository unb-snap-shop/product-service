class Component(dict):
    def __init__(self, id, type, brand, model, specifications, price):
        self.id = id
        self.type = type
        self.brand = brand
        self.model = model
        self.specifications = specifications
        self.price = price

        dict.__init__(self, id=id, type = type , brand = brand, model=model, specifications = specifications, price=price)

class CPU(Component):
    def __init__(self, id, brand, model, specifications, price):
        super().__init__(id, 'CPU', brand, model, specifications, price)

   
class GPU(Component):
    def __init__(self, id, brand, model, specifications, price):
        super().__init__(id, 'GPU', brand, model, specifications, price)


class Motherboard(Component):
    def __init__(self, id, brand, model, specifications, price):
        super().__init__(id, 'Motherboard', brand, model, specifications, price)

class RAM(Component):
    def __init__(self, id, brand, model, specifications, price):
        super().__init__(id, 'RAM', brand, model, specifications, price)

class Storage(Component):
    def __init__(self, id, brand, model, specifications, price):
        super().__init__(id, 'Storage', brand, model, specifications, price)