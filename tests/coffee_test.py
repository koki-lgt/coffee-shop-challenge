import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

class TestCoffee:
    def test_name_validation(self):
        coffee = Coffee("Frappe")

        with pytest.raises(AttributeError):
            coffee.name = "Macchiato"

        with pytest.raises(TypeError):
            Coffee(123)
        with pytest.raises(ValueError):
            Coffee("A")

    def test_relationships(self):
        coffee = Coffee("Frappe")
        customer1 = Customer("Lina")
        customer2 = Customer("John")

        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 8.0)

        assert len(coffee.orders()) == 2
        assert len(coffee.customers()) == 2
        assert customer1 in coffee.customers()

    def test_aggregate_methods(self):
        coffee = Coffee("Frappe")
        customer = Customer("John")

        assert coffee.num_orders() == 0
        assert coffee.average_price() == 0

        Order(customer, coffee, 5.0)
        Order(customer, coffee, 8.0)

        assert coffee.num_orders() == 2
        assert coffee.average_price() == 6.5
