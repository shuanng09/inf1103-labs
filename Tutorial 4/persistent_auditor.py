import os

FILENAME = "orders.txt"

def load_inventory():
    orders = []
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(",")
                        if len(parts) == 3:
                            orders.append({
                                "id": int(parts[0].strip()),
                                "name": parts[1].strip(),
                                "quantity": int(parts[2].strip())
                            })
        except Exception as e:
            print(f"Error loading file: {e}")
    return orders

def save_inventory(orders):
    """Saves the full orders list back to orders.txt"""
    try:
        with open(FILENAME, "w") as file:
            for order in orders:
                file.write(f"{order['id']},{order['name']},{order['quantity']}\n")
        print(f"Order successfully saved to {FILENAME}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def generate_report(orders, failed_attempts):
    """Prints the final audit summary report when the user quits."""
    total_transactions = len(orders)
    total_units = sum(order["quantity"] for order in orders)

    print("\n--- AUDIT REPORT ---")
    print(f"Total transaction recorded : {total_transactions}")
    print(f"Total unit processed       : {total_units}")
    print(f"Number of failed           : {failed_attempts}\n")

def main():
    orders = load_inventory()
    transaction_history = []
    failed_entries = 0

    print("Current Orders:\n")
    if orders:
        for order in orders:
            print(f"{order['id']}, {order['name']}, {order['quantity']}")
            transaction_history.append(f"{order['id']},{order['name']},{order['quantity']}")
    else:
        print("No previous orders found.")

    while True:
        next_id = orders[-1]["id"] + 1 if orders else 1001

        print()
        product_name = input("Enter Product Name (or type 'quit' to exit): ").strip()

        # Handle 'quit' at product name prompt
        if product_name.lower() == 'quit':
            generate_report(orders, failed_entries)
            save_inventory(orders)
            break

        if not product_name:
            print("Error: Product name cannot be empty.")
            failed_entries += 1
            continue

        while True:
            qty_input = input("Enter Quantity: ").strip()

            # Handle 'quit' at quantity prompt
            if qty_input.lower() == 'quit':
                generate_report(orders, failed_entries)
                save_inventory(orders)
                return

            if qty_input.isdigit() and int(qty_input) >= 0:
                quantity = int(qty_input)
                break

            print("Error: Invalid quantity. Please enter a valid non-negative integer.")
            failed_entries += 1

        new_order = {"id": next_id, "name": product_name, "quantity": quantity}
        orders.append(new_order)

        formatted_order = f"{next_id},{product_name},{quantity}"
        transaction_history.append(formatted_order)

        print("\nNew Order Added:")
        print(formatted_order)

if __name__ == "__main__":
    main()