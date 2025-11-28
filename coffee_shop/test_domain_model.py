import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_order_relationship():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee)
    
    assert len(customer.orders) == 1
    assert customer.orders[0] == order

def test_coffee_order_relationship():
    customer = Customer("Bob")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee)
    
    assert len(coffee.orders) == 1
    assert coffee.orders[0] == order

def test_many_to_many_relationship():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    
    order1 = Order(customer1, coffee1)
    order2 = Order(customer1, coffee2)
    order3 = Order(customer2, coffee1)
    
    assert len(customer1.orders) == 2
    assert len(customer2.orders) == 1
    assert len(coffee1.orders) == 2
    assert len(coffee2.orders) == 1