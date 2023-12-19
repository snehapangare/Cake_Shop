class Cake:
    def __init__(self, cake_id, flavor, size, quantity,price):
        self.cake_id = cake_id
        self.flavor = flavor
        self.size = size
        self.quantity=quantity
        self.price = price

    def __str__(self):
        data = f"{self.cake_id},{self.flavor},{self.size},{self.quantity},{float(self.price)}"
        return data