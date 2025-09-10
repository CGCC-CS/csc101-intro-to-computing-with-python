'''
Comparing different data structures in Python
'''

# Same data in different structures
data = [1, 2, 3, 2, 4, 2, 5]

as_list = [1, 2, 3, 2, 4, 2, 5]
as_tuple = (1, 2, 3, 2, 4, 2, 5)
as_set = {1, 2, 3, 4, 5}  # Duplicates removed
as_dict = {0: 1, 1: 2, 2: 3, 3: 2, 4: 4, 5: 2, 6: 5}  # Index as key

print("Same data in different structures:")
print(f"List:  {as_list}")
print(f"Tuple: {as_tuple}")
print(f"Set:   {as_set}")
print(f"Dict:  {as_dict}")

print("\nCharacteristics comparison:")
print(f"{'Structure':<10} {'Ordered':<8} {'Mutable':<8} {'Duplicates':<10} {'Indexed':<8}")
print(f"{'List':<10} {'Yes':<8} {'Yes':<8} {'Yes':<10} {'Yes':<8}")
print(f"{'Tuple':<10} {'Yes':<8} {'No':<8} {'Yes':<10} {'Yes':<8}")
print(f"{'Set':<10} {'No':<8} {'Yes':<8} {'No':<10} {'No':<8}")
print(f"{'Dict':<10} {'Yes*':<8} {'Yes':<8} {'Values':<10} {'Keys':<8}")

# Demonstrate access patterns
print("\nAccess patterns:")
print(f"List[1]:  {as_list[1]}")
print(f"Tuple[1]: {as_tuple[1]}")
# print(f"Set[1]:   Not supported")  # Sets don't support indexing
print(f"Dict[1]:  {as_dict[1]}")

# Demonstrate mutability
original_list = as_list.copy()
as_list[1] = 'changed'
print("\nMutability test:")
print(f"Original list: {original_list}")
print(f"Modified list: {as_list}")

try:
    as_tuple[1] = 'changed'
except TypeError as e:
    print(f"Tuple modification error: {e}")
