class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
    
    @property
    def orders(self):
        return self._orders
    
    def add_order(self, order):
        self._orders.append(order)