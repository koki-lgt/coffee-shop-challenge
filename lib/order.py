class Order:
    all = []

    def __init__(self, customer, coffee, price: float):
        from lib.customer import Customer
        from lib.coffee import Coffee
        
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        
        if customer.__class__.__name__ != 'Customer':
            raise TypeError("Customer must be of type Customer")
        if coffee.__class__.__name__ != 'Coffee':
            raise TypeError("Coffee must be of type Coffee")
        
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)
        customer.orders().append(self)


    @property
    def price(self):
        return self._price
    
        
        