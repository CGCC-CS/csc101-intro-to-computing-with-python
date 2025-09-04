"""
This program calculates the area of a circle while demonstrating proper
documentation & naming practices.

Author: Wade Huber
Date: August 23, 2025
"""

import math

# Get radius from user
radius = float(input("Enter the radius of the circle: "))

# Calculate area using the formula: A = π * r²
area = math.pi * radius ** 2

# Display the result with proper formatting
print(f"The area of a circle with radius {radius} is {area:.2f}")