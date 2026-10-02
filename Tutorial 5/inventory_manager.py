import json
import os

FILENAME = "inventory.json"


def get_default_items():
    """Returns the default initial items required by Requirement 1."""
    return [
        {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    ]


def load_inventory():
    """Loads inventory from inventory.json.

    If missing or empty, populates it with default items.
    """
    default_items = get_default_items()

    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                inventory = json.load(file)

            # If the file exists but has no items in it [], reset with defaults
            if not inventory:
                print("inventory.json found but was empty.")
                print("Populating initial items...")
                save_inventory(default_items)
                return default_items

            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return inventory
        except Exception as e:
            print(f"Error loading file: {e}")
            save_inventory(default_items)
            return default_items
    else:
        print(
            "inventory.json not found. Initializing file with default items..."
        )
        save_inventory(default_items)
        return default_items


def save_inventory(inventory):
    """Saves the inventory data to inventory.json."""
    try:
        with open(FILENAME, "w") as file:
            json.dump(inventory, file, indent=4)
        print("Inventory saved successfully to inventory.json.")
    except Exception as e:
        print(f"Error saving to file: {e}")


def display_all(inventory):
    """Displays all products formatted to match the required layout."""
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
    """Adds a new product to the inventory with auto-generated ID."""
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
    """Updates stock quantity for an existing product by ID."""
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
    """Searches and displays product details by ID."""
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


def display_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 32)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 32)
    print("\n---------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")


def main():
    inventory = load_inventory()

    while True:
        display_menu()
        option = input("\nEnter option: ").strip()

        if option == "1":
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()