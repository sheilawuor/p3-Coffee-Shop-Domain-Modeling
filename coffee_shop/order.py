class Order:
    def __init__(self, customer, coffee, price):
        if price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        customer.add_order(self)
        coffee.add_order(self)