''' 
Demonstrates empty collections and their properties in Python
'''

# Empty collections
empty_string = ''
empty_list = []
empty_tuple = ()
empty_set = set()  # Note: {} creates an empty dict, not set
empty_dict = {}

print("Empty collections:")
print(f"Empty string: '{empty_string}'")
print(f"Empty list: {empty_list}")
print(f"Empty tuple: {empty_tuple}")
print(f"Empty set: {empty_set}")
print(f"Empty dict: {empty_dict}")

# Lengths of empty collections
print("\nLengths:")
print(f"len(empty_string): {len(empty_string)}")  # Quiz answer: 0
print(f"len(empty_list): {len(empty_list)}")
print(f"len(empty_tuple): {len(empty_tuple)}")
print(f"len(empty_set): {len(empty_set)}")
print(f"len(empty_dict): {len(empty_dict)}")

# Testing for emptiness
print("\nBoolean tests (empty = False):")
print(f"bool(empty_string): {bool(empty_string)}")
print(f"bool(empty_list): {bool(empty_list)}")
print(f"bool(empty_tuple): {bool(empty_tuple)}")
print(f"bool(empty_set): {bool(empty_set)}")
print(f"bool(empty_dict): {bool(empty_dict)}")

# Adding to empty collections
empty_list.append('first item')
empty_set.add('first item')
empty_dict['first_key'] = 'first value'

print("\nAfter adding items:")
print(f"List: {empty_list}")
print(f"Set: {empty_set}")
print(f"Dict: {empty_dict}")
