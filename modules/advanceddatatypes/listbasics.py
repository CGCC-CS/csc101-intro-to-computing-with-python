''' 
Demonstrates list creation, indexing, slicing, and basic operations
'''

# Creating lists
my_list = [2, 8, 3, 1, 18, 5]
city_codes = ['SFO', 'ORD', 'ATL', 'SEA']
mixed_list = [1, 'hello', 3.14, True]

print("List examples:")
print(f"Numbers: {my_list}")
print(f"City codes: {city_codes}")
print(f"Mixed types: {mixed_list}")

# List indexing and length
print("\nList indexing:")
print(f"my_list[0] = {my_list[0]}")  # First element
print(f"my_list[3] = {my_list[3]}")  # Fourth element
print(f"my_list[-1] = {my_list[-1]}")  # Last element
print(f"Length of my_list: {len(my_list)}")

# List slicing
print("\nList slicing:")
print(f"First 3 elements: {my_list[:3]}")
print(f"Last 3 elements: {my_list[-3:]}")
print(f"Middle elements: {my_list[1:4]}")

# Mathematical operations with lists
print("\nMath with list elements:")
result = my_list[3] + my_list[1] * 2  # Quiz example: 1 + 8*2 = 17
print(f"my_list[3] + my_list[1] * 2 = {result}")

# List properties
print("\nList properties:")
print(f"city_codes[1] = '{city_codes[1]}'")
print(f"Length of city_codes: {len(city_codes)}")
print(f"Index of last item: {len(city_codes) - 1}")  # Not 4!
