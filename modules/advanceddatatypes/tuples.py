''' 
Demonstrates tuple creation, indexing, unpacking, and immutability in Python
'''

# Creating tuples
coordinates = (10, 20)
rgb_color = (255, 128, 64)
mixed_tuple = (1, 'hello', 3.14, True)
single_item = (42,)  # Note the comma for single-item tuple

print("Tuple examples:")
print(f"Coordinates: {coordinates}")
print(f"RGB color: {rgb_color}")
print(f"Mixed tuple: {mixed_tuple}")
print(f"Single item: {single_item}")

# Tuple indexing (same as lists)
print("\nTuple indexing:")
print(f"coordinates[0] = {coordinates[0]}")
print(f"rgb_color[-1] = {rgb_color[-1]}")
print(f"Length of mixed_tuple: {len(mixed_tuple)}")

# Tuple unpacking
x, y = coordinates
r, g, b = rgb_color
print(f"\nUnpacked coordinates: x={x}, y={y}")
print(f"Unpacked color: r={r}, g={g}, b={b}")

# Tuples are immutable
print("\nImmutability test:")
try:
    coordinates[0] = 15  # This will cause an error
except TypeError as e:
    print(f"Error: {e}")

# But you can create new tuples
new_coordinates = (15, 25)
print(f"New coordinates: {new_coordinates}")

# Tuple methods (limited compared to lists)
numbers = (1, 2, 3, 2, 4, 2, 5)
print("\nTuple methods:")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")
