class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = value
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(order.coffee for order in self._orders))
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        customer_totals = {}
        for order in coffee.orders():
            customer = order.customer
            customer_totals[customer] = customer_totals.get(customer, 0) + order.price
        return max(customer_totals, key=customer_totals.get)
    
    def add_order(self, order):
        self._orders.append(order)