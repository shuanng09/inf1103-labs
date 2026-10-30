import json
from product import Product
from inventory import Inventory

def load_inventory(filename="inventory.json") -> Inventory:
    inventory = Inventory()
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            for item in data:
                prod = Product(item["id"], item["name"], item["price"], item["stock"])
                inventory.add_product(prod)
    except FileNotFoundError:
        print("No existing inventory file found. Starting fresh.")
    return inventory

def save_inventory(inventory: Inventory, filename="inventory.json") -> None:
    data = [product.to_dict() for product in inventory.products]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print("Inventory saved successfully.")

def main():
    inventory = load_inventory()

    while True:
        print("\n=== Inventory Management System ===")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Enter option (1-6): ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            p_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))
            new_prod = Product(p_id, name, price, stock)
            inventory.add_product(new_prod)
            print("Product added successfully!")

        elif choice == "3":
            p_id = input("Enter Product ID to update: ")
            prod = inventory.search_product(p_id)
            if prod:
                qty = int(input("Enter stock adjustment (e.g., +10 or -5): "))
                prod.update_stock(qty)
                print("Stock updated successfully.")
            else:
                print("Product not found.")

        elif choice == "4":
            p_id = input("Enter Product ID to search: ")
            prod = inventory.search_product(p_id)
            if prod:
                prod.display_information()
            else:
                print("Product not found.")

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()