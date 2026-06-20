class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")