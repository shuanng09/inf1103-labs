from inventory import Inventory
from product_types import DigitalProduct, PhysicalProduct


def main():
  inv = Inventory()

  while True:
    print("\n--- Inventory Management System ---")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save & Exit")

    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
      inv.display_all()

    elif choice == "2":
      p_type = (
          input("Product Type (1: Physical, 2: Digital): ").strip().lower()
      )
      p_id = input("ID: ").strip()
      name = input("Name: ").strip()
      price = float(input("Price: "))
      stock = int(input("Stock: "))

      if p_type in ["1", "physical"]:
        weight = float(input("Weight (kg): "))
        product = PhysicalProduct(p_id, name, price, stock, weight)
      elif p_type in ["2", "digital"]:
        size = float(input("Download Size (MB): "))
        product = DigitalProduct(p_id, name, price, stock, size)
      else:
        print("Invalid product type.")
        continue

      inv.add_product(product)
      print("Product added successfully.")

    elif choice == "3":
      p_id = input("Product ID: ").strip()
      product = inv.search_product(p_id)
      if product:
        qty = int(input("Stock adjustment (e.g. +5 or -2): "))
        product.update_stock(qty)
        print("Stock updated.")
      else:
        print("Product not found.")

    elif choice == "4":
      p_id = input("Product ID: ").strip()
      product = inv.search_product(p_id)
      if product:
        product.display_information()
        print(f"Fulfilment: {product.get_fulfilment_info()}")
      else:
        print("Product not found.")

    elif choice == "5":
      inv.save_data()
      print("Inventory saved. Exiting...")
      break


if __name__ == "__main__":
  main()