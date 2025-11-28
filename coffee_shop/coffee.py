class Coffee:
    def __init__(self, name):
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self.name = name
        self._orders = []
    
    def orders(self):
        return self._orders
    
    def customers(self):
        unique_customers = []
        for order in self._orders:
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if len(self._orders) == 0:
            return 0
        
        total_price = 0
        for order in self._orders:
            total_price += order.price
        
        return total_price / len(self._orders)
    
    def add_order(self, order):
        self._orders.append(order)