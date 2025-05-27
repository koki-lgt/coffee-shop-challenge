class Customer():
    def __init__(self, name):
        self.name = name
        self._orders = []


    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders
    
    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        from lib.order import Order
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        
        customers = {}
        for order in coffee.orders():
            if order.customer in customers:
                customers[order.customer] += order.price
            else:
                customers[order.customer] = order.price

        return max(customers.items(), key=lambda x: x[1])[0]


    

        
        
    