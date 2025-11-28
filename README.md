# Coffee Shop Domain Model

A simple Python domain model for a coffee shop with three main classes:

## Classes

- **Customer**: Represents a coffee shop customer
- **Coffee**: Represents a type of coffee
- **Order**: Represents an order linking a customer to a coffee

## Setup

```bash
cd coffee_shop
pipenv install
pipenv shell
```

## Usage

```python
from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
customer = Customer("Alice")
coffee = Coffee("Latte")
order = Order(customer, coffee, 4.50)

# Check relationships
print(customer.orders())  # List of orders
print(coffee.customers())  # List of customers
```
