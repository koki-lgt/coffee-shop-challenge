import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

class TestOrder:
    def test_validation(self):
        customer = Customer("Lina")
        coffee = Coffee("Macchiato")

        Order(customer, coffee, 1.0)
        Order(customer, coffee, 10.0)

        with pytest.raises(TypeError):
            Order("NotCusttomer", coffee, 5.0)
        with pytest.raises(TypeError):
            Order(customer, "NotCoffee",5.0 )
        with pytest.raises(TypeError):
            Order(customer, coffee, 5)
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.99)
        with pytest.raises(ValueError):
            Order(customer, coffee, 10.01)

    def test_price_immutability(self):
        customer = Customer("Lina")
        coffee = Coffee("Frappe")
        order = Order(customer, coffee, 5.0)

        with pytest.raises(AttributeError):
            order.price = 5.0

    def test_relationships(self):
        customer = Customer("Lina")
        coffee = Coffee("Frappe")
        order = Order(customer, coffee, 5.0)

        assert order.customer == customer
        assert order.coffee == coffee
        assert order in Order.all
        assert order in customer.orders()
