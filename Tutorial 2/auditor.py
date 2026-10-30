total_inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
    
    if user_input.lower() == "quit":
        break
        
    if not user_input.isdigit():
        print("Error: Invalid entry. Please enter a valid non-negative integer.")
        failed_entries += 1
        continue
        
    quantity = int(user_input)
    
    if quantity < 0:
        print("Error: Quantity cannot be negative.")
        failed_entries += 1
        continue
        
    total_inventory += quantity
    
    if total_inventory > 500:
        print(f"OVERSTOCK ALERT: Inventory total ({total_inventory}) exceeded 500 units!")
        break

print(f"\nTotal Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")