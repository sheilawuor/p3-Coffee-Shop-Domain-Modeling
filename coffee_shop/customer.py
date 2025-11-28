class Customer:
    def __init__(self, name):
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self.name = name
        self._orders = []
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        unique_coffees = []
        for order in self._orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        if len(coffee.orders()) == 0:
            return None
        
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            if customer in customer_spending:
                customer_spending[customer] += order.price
            else:
                customer_spending[customer] = order.price
        
        highest_spender = None
        highest_amount = 0
        for customer, amount in customer_spending.items():
            if amount > highest_amount:
                highest_amount = amount
                highest_spender = customer
        
        return highest_spender
    
    def add_order(self, order):
        self._orders.append(order)