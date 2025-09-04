"""
A simple calculator program that performs basic arithmetic operations
(addition, subtraction, multiplication, division) on two user-input numbers.

This program does not handle invalid inputs or division by zero.
"""

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations:w

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

# Display results
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")