from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def search_product(self, product_id: str) -> Product:
        for product in self.products:
            if product._product_id.lower() == product_id.lower():
                return product
        return None

    def display_all(self) -> None:
        if not self.products:
            print("No products in inventory.")
            return
        print("\n--- Current Inventory ---")
        for product in self.products:
            product.display_information()