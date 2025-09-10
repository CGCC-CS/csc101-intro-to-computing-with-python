''' 
Demonstrates list methods: 
    append, insert, remove, pop, extend, sort, reverse, count, index
'''

# Starting with a list
fruits = ['apple', 'banana', 'cherry']
print(f"Original list: {fruits}")

# Adding elements
fruits.append('date')  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, 'blueberry')  # Insert at index 1
print(f"After insert: {fruits}")

# Extending with another list
more_fruits = ['elderberry', 'fig']
fruits.extend(more_fruits)
print(f"After extend: {fruits}")

# Removing elements
fruits.remove('banana')  # Remove by value
print(f"After remove: {fruits}")

popped = fruits.pop()  # Remove and return last item
print(f"Popped item: {popped}")
print(f"After pop: {fruits}")

popped_index = fruits.pop(0)  # Remove and return item at index 0
print(f"Popped from index 0: {popped_index}")
print(f"Final list: {fruits}")

# Other useful methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nNumbers: {numbers}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 4: {numbers.index(4)}")

# Sorting
numbers.sort()
print(f"Sorted: {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")
