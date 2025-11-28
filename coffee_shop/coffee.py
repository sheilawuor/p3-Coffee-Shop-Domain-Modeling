class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Name must be a string at least 3 characters long")
        self._name = value
    
    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(order.customer for order in self._orders))
    
    def add_order(self, order):
        self._orders.append(order)