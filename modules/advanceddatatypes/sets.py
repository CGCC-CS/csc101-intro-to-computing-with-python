''' 
Demonstrates set creation, operations, and methods in Python
'''

# Creating sets
car_brands = {'Toyota', 'Honda', 'Ford', 'Chevrolet'}
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, 'hello', 3.14}

print("Set examples:")
print(f"Car brands: {car_brands}")
print(f"Numbers: {numbers}")
print(f"Mixed set: {mixed_set}")

# Sets automatically remove duplicates
duplicate_numbers = {1, 2, 2, 3, 3, 3, 4}
print(f"Duplicates removed: {duplicate_numbers}")

# Set operations
print("\nSet operations:")
print(f"Length: {len(car_brands)}")
print(f"Is 'Ford' in set: {'Ford' in car_brands}")
print(f"Is 'BMW' in set: {'BMW' in car_brands}")

# Adding and removing elements
car_brands.add('BMW')
print(f"After adding BMW: {car_brands}")

car_brands.remove('Ford')  # Removes 'Ford' or raises KeyError if not found
print(f"After removing Ford: {car_brands}")

# Alternative removal methods
car_brands.discard('Nissan')  # Won't raise error if not found
print(f"After discard (no error): {car_brands}")

# Pop removes arbitrary element
popped = numbers.pop()
print(f"Popped from numbers: {popped}")
print(f"Numbers after pop: {numbers}")

# Set operations with other sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nSet operations between {set1} and {set2}:")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")