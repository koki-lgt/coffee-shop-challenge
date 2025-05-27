import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order


class TestCustomer:
    def test_name_validation(self):
        Customer("A")
        Customer("123456789")

        with pytest.raises(TypeError):
            Customer(123)
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")

    def test_relationships(self):
        customer = Customer("Lina")
        coffee1 = Coffee("Frappe")
        coffee2 = Coffee("Machiatto")

        order1 = Order(customer, coffee1, 5.0)
        order2 = Order(customer, coffee2, 4.5)

        assert len(customer.orders()) == 2
        assert len(customer.coffees()) == 2
        assert coffee1 in customer.coffees()

    def test_create_order(self):
        customer = Customer("John")
        coffee = Coffee("Frappe")
        order = customer.create_order(coffee, 5.0)

        assert isinstance(order, Order)
        assert order in customer.orders()
        assert order.coffee == coffee

    def test_most_aficionado(self):
        coffee = Coffee("Frappe")
        customer1 = Customer("Lina")
        customer2 = Customer("John")

        assert Customer.most_aficionado(coffee) is None

        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 8.0)

        assert Customer.most_aficionado(coffee) == customer2
