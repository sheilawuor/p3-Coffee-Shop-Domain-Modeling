class Order:
    def __init__(self, customer, coffee):
        self.customer = customer
        self.coffee = coffee
        customer.add_order(self)
        coffee.add_order(self)