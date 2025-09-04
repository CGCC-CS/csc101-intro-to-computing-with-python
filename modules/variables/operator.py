"""
This module demonstrates the use of operators in Python.

Author: Wade Huber
Date: August 23, 2025
"""
# Define some variables to use
# Normally, a & b are bad variable names, but we use them here to keep it short
a = 10
b = 3

# Perform basic arithmetic operations
addition = a + b        # Addition: 10 + 3 = 13
subtraction = a - b     # Subtraction: 10 - 3 = 7
multiplication = a * b  # Multiplication: 10 * 3 = 30
division = a / b        # Division: 10 / 3 = 3.333...
floor_division = a // b # Integer division: 10 // 3 = 3
modulus = a % b         # Modulus: 10 % 3 = 1
exponentiation = a ** b # Exponentiation: 10 ** 3 = 1000

print(f"Results: {addition}, {subtraction}, {multiplication}, {division}")
print(f"Division: {division:.2f}, Floor: {floor_division}, Remainder {modulus}")

