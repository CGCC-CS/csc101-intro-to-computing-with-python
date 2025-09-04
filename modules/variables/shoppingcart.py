"""
Shopping Cart Total Calculator
Combines: data types, variables, operators, expressions, input/output, formatting

This program does NOT check for invalid inputs or exceptions

Author: Wade Huber
Date: August 23, 2025
"""

# Store information using different data types
store_name = "Python Grocery Store"
tax_rate = 0.0825  # 8.25% tax rate
item_count = 0
subtotal = 0.0

print(f"Welcome to {store_name}!")
print("Enter items (enter 0 for price to finish):")

# Collect items using a simple loop concept
while True:
    item_name = input("Item name: ")
    item_price = float(input("Item price: $"))
    
    if item_price == 0:  # Exit condition: if user enters $0 for price
        break
    
    # Update running totals using assignment operators
    item_count += 1
    subtotal += item_price
    
    print(f"Added: {item_name} - ${item_price:.2f}")

# Calculate final amounts using expressions
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

# Format and display receipt
print(f"\n{'='*30}")
print(f"{store_name.upper()}")
print(f"{'='*30}")
print(f"Items purchased: {item_count}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax ({tax_rate*100:.2f}%): ${tax_amount:.2f}")
print(f"TOTAL: ${total:.2f}")
print(f"{'='*30}")

# Boolean expressions for analysis
is_large_purchase = total > 100
has_tax = tax_amount > 0
print(f"Large purchase (>$100): {is_large_purchase}")
print(f"Tax applied: {has_tax}")