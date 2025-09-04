""" 
This module demonstrates the use of variables in Python.

Author: Wade Huber
Date: August 23, 2025
"""

# Store student information and pricing details
student_name = "John"        # snake_case for variables
DISCOUNT_RATE = 0.15         # UPPER_CASE for constants
total_price = 100.0
print(f"Student: {student_name}")
print(f"Original price: ${100.0:.2f}")

# Variable reassignment
# Update student name and apply discount to price
student_name = "Jane"
total_price = total_price * (1 - DISCOUNT_RATE)

print(f"New Student: {student_name}")
print(f"Discount applied: {DISCOUNT_RATE*100:.0f}%")
print(f"Final price: ${total_price:.2f}")