from product import Product
from product_manager import ProductManager
from cart import Cart


manager = ProductManager()

product1 = Product("Laptop", 1000, 10)
product2 = Product("Mouse", 25, 50)
product3 = Product("Keyboard", 60, 20)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

print("PRODUCT LIST")
manager.display_products()

cart = Cart()

cart.add_to_cart(product1, 1)
cart.add_to_cart(product2, 2)

print()
cart.display_cart()