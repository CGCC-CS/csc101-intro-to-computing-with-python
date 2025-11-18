# map() - Apply function to all items
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert to uppercase
names = ["alice", "bob", "charlie"]
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# filter() - Keep only items that meet condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Keep names longer than 4 characters
names = ["Ann", "Robert", "Joe", "Elizabeth"]
long_names = list(filter(lambda name: len(name) > 4, names))
print(long_names)  # ['Robert', 'Elizabeth']

# sorted() - Custom sorting
# Sort by absolute value
numbers = [-5, 2, -8, 1, 9, -3]
sorted_nums = sorted(numbers, key=lambda x: abs(x))
print(sorted_nums)  # [1, 2, -3, -5, -8, 9]

# Sort students by grade
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print(sorted_students)
# [{'name': 'Bob', 'grade': 92}, {'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 78}]

