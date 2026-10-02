import json
import os

FILENAME = "inventory.json"

def get_initial_products():
    """Returns initial inventory represented as a list of dictionaries (Req 1)."""
    return [
        {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    ]


def display_all(inventory):
    """Displays all products formatted to match the output requirements (Req 2)."""
    print("\nCurrent Inventory")
    print("-" * 50)
    if not inventory:
        print("No products available.")
    else:
        for item in inventory:
            print(
                f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}"
            )
    print("-" * 50)


def add_product(inventory):
    """Adds a new product to the inventory list (Req 2)."""
    print("\nAdd New Product")

    if inventory:
        last_id_num = int(inventory[-1]["id"].replace("P", ""))
        next_id = f"P{last_id_num + 1:03d}"
    else:
        next_id = "P001"

    print(f"Product ID: {next_id}")
    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid input for price or stock. Product not added.")
        return

    inventory.append(
        {"id": next_id, "name": name, "price": price, "stock": stock}
    )
    print("\nProduct added successfully!")


def update_stock(inventory):
    """Updates stock quantity for an existing product (Req 2)."""
    print("\nUpdate Stock")
    prod_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"].lower() == prod_id.lower():
            print("\nProduct Found:")
            print(f"Name: {item['name']}")
            print(f"Current Stock: {item['stock']}\n")

            try:
                new_stock = int(input("New Stock Quantity: "))
                item["stock"] = new_stock
                print("\nStock updated successfully!")
            except ValueError:
                print("Invalid stock quantity entered.")
            return

    print("\nProduct not found.")


def search_product(inventory):
    """Searches and displays product details by ID (Req 2)."""
    print("\nSearch Product")
    prod_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"].lower() == prod_id.lower():
            print("\nProduct Found")
            print("-" * 45)
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Stock: {item['stock']}")
            print("-" * 45)
            return

    print("\nProduct not found.")



def load_inventory():
    """Checks whether inventory.json exists and loads data.

    Initializes with default items if missing or empty (Req 3).
    """
    default_items = get_initial_products()

    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                inventory = json.load(file)

            if not inventory:
                print(
                    "inventory.json found but was empty. Loading default items..."
                )
                return default_items

            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return inventory
        except Exception as e:
            print(f"Error loading file: {e}")
            return default_items
    else:
        print(
            "inventory.json not found. Initializing with sample products..."
        )
        return default_items

if __name__ == "__main__":
    print("--- TESTING PHASE A + B ---")
    # Test load_inventory()
    inventory = load_inventory()

    # Test display_all()
    display_all(inventory)