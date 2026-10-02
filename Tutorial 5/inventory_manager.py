# Phase A: Inventory Management Core System


def get_initial_products():
    """Returns initial inventory represented as a list of dictionaries."""
    return [
        {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    ]


def display_all(inventory):
    """Displays all products formatted to match requirements."""
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
    """Adds a new product to the inventory dictionary list."""
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
    """Updates stock quantity for an existing product."""
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