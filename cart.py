class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
            print(f"{quantity} x {product.name} added to cart.")
        else:
            print("Not enough stock.")

    def calculate_total(self):
        total = 0

        for product, quantity in self.items:
            total += product.price * quantity

        return total

# Cart functionality branch update
    def display_cart(self):
        print("Shopping cart:")

        for product, quantity in self.items:
            print(f"{product.name} - {quantity} pcs")

        print(f"Total: {self.calculate_total()}")
