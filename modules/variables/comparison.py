"""
This module demonstrates the use of comparison operators in Python.

Author: Wade Huber
Date: August 23, 2025
"""

# Some variables to work with
num1 = 10
num2 = 5

# Comparison operators
print(f"{num1} > {num2}: {num1 > num2}")      # greater than
print(f"{num1} < {num2}: {num1 < num2}")      # less than
print(f"{num1} >= {num2}: {num1 >= num2}")    # greater than or equal to
print(f"{num1} <= {num2}: {num1 <= num2}")    # less than or equal to
print(f"{num1} == {num2}: {num1 == num2}")    # equal to
print(f"{num1} != {num2}: {num1 != num2}")    # not equal to

# Logical operators
is_positive = num1 > 0
is_even = num1 % 2 == 0
is_positive_and_even= is_positive and not is_even
is_positive_or_even = is_positive or is_even

print(f"x is positive and odd: {is_positive_and_even}")
print(f"x is positive or even: {is_positive_or_even}")
