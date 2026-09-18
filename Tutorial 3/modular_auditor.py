# total_inventory = 0
# failed_entries = 0


# while True:
#     user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
    
#     if user_input.lower() == "quit":
#         print("Total Deliveries Processed" ,"Number of Failed/Rejected Entries:")
#         break
        
#     if not user_input.isdigit():
#         print("Error: Invalid entry. Please enter a valid non-negative integer.")
#         failed_entries += 1
#         continue
        
#     quantity = int(user_input)
    
    
#     if quantity < 0:
#         print("Error: Quantity cannot be negative.")
#         failed_entries += 1
#         continue
        
#     total_inventory += quantity
    
#     if total_inventory > 500:
#         print(f"OVERSTOCK ALERT: Inventory total ({total_inventory}) exceeded 500 units!")
#         break

# print(f"\nTotal Units Processed: {total_inventory}")
# print(f"Number of Failed/Rejected Entries: {failed_entries}")


def get_valid_input():

    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
         return "quit"
    
    if not user_input.isdigit():
          print("Error: Invalid entry. Please enter a valid non-negative integer.")
          return None

    quantity = int(user_input)
    if quantity < 0:
         print("Error: Quantity cannot be negative.")
         failed_entries += 1
         return None

    return quantity

def process_delivery(current_total, new_value):
     return current_total + new_value

def calculate_tax(amount):
     return amount * 0.10

def generate_report(total_units, failed_attempts):
    """Prints the final summary report."""
    print("\n--- AUDIT REPORT ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

def main():
     total_inventory = 0
     failed_entries = 0

     while True:
          value = get_valid_input()

          if value == "quit":
            break

          if value is None:
               failed_entries += 1
               continue

          total_inventory = process_delivery(total_inventory, value)
          tax = calculate_tax(value)

          print(f"Accepted: {value} units | Tax for this delivery: {tax:.2f} | Running Total: {total_inventory}")

          generate_report(total_inventory, failed_entries)


if __name__ == "__main__":
    main()






    
    