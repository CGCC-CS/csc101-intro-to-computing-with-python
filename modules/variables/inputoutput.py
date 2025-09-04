"""
This example demonstrates getting user input and displaying formatted output.

Author: Wade Huber
Date: August 23, 2025
"""

# Getting user input and formatted output
# Note that here we are assuming the user gives valid input
#    we will cover how to handle input errors in a later module
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

# Formatted output using f-strings
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your GPA is {gpa:.2f}")
print("Pi is {:.2f}".format(3.14159))  # old style formatting