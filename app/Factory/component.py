class Component:
    def __init__(self, id, type, brand, model, specifications, price):
        self.id = id
        self.type = type
        self.brand = brand
        self.model = model
        self.specifications = specifications
        self.price = price

class CPU(Component):
    def __init__(self, id, brand, model, cores, threads, base_clock, boost_clock, tdp, price):
        specifications = {
            'cores': cores,
            'threads': threads,
            'baseClock': base_clock,
            'boostClock': boost_clock,
            'tdp': tdp
        }
        super().__init__(id, 'CPU', brand, model, specifications, price)

   
class GPU(Component):
    def __init__(self, id, brand, model, memory, boost_clock, tdp, price):
        specifications = {
            'memory': memory,
            'boostClock': boost_clock,
            'tdp': tdp
        }
        super().__init__(id, 'GPU', brand, model, specifications, price)

class Motherboard(Component):
    def __init__(self, id, brand, model, chipset, memory, formFactor, price):
        specifications = {
            'chipset' : chipset,
            'memory' : memory,
            'formFactor' : formFactor
        }
        super().__init__(id, 'Motherboard', brand, model, specifications, price)

class RAM(Component):
    def __init__(self, id, brand, model, memory_type, speed, modules, latency, price):
        specifications = {
            'memoryType': memory_type,  
            'speed': speed,
            'modules': modules, 
            'latency': latency 
        }
        super().__init__(id, 'RAM', brand, model, specifications, price)

class Storage(Component):
    def __init__(self, id, brand, model, storage_type, formFactor, interface, rpm, cache, price):
        specifications = {
            'storageType': storage_type, 
            'formFactor': formFactor,
            'interface': interface,
            'rpm': rpm,
            'cache': cache
        }
        super().__init__(id, 'Storage', brand, model, specifications, price)