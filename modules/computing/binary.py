"""
Binary Number Converter

This module provides a simple interactive program for converting between
decimal and binary number systems. Users can choose to convert:
1. Decimal numbers to binary representation
2. Binary numbers to decimal representation

The program uses Python's built-in bin() function for decimal-to-binary
conversion and int() with base 2 for binary-to-decimal conversion.

Author: Wade Huber
Date: August 12, 2025

"""

print("Binary Number Converter")
print("1. Decimal to Binary")
print("2. Binary to Decimal")

choice = input("Choose 1 or 2: ")

if choice == "1":
    decimal = int(input("Enter a decimal number: "))
    binary = bin(decimal)[2:]  # bin returns a'0b' prefix, so we remove it
    print("Binary version:", binary)
elif choice == "2":
    binary = input("Enter a binary number (like 1010): ")
    decimal = int(binary, 2)
    print("Decimal version:", decimal)
else:
    print("Invalid choice")
