from product import Product


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display_info()
            print("-" * 20)

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def remove_product(self, name):
        product = self.find_product(name)

        if product:
            self.products.remove(product)
            print(f"Product {name} removed successfully.")
        else:
            print(f"Product {name} not found.")