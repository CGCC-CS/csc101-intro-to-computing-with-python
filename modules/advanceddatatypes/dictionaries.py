'''
Demonstrates dictionary creation, access, modification, and methods
'''

# Creating dictionaries
student = {
    'name': 'Alice',
    'age': 20,
    'major': 'Computer Science',
    'gpa': 3.85
}

fruits_dict = {
    'Apple': 1.50,
    'Banana': 0.75,
    'Orange': 1.25,
    'Lemon': 0.50
}

print("Dictionary examples:")
print(f"Student: {student}")
print(f"Fruit prices: {fruits_dict}")

# Accessing values
print("\nAccessing values:")
print(f"Student name: {student['name']}")
print(f"Apple price: ${fruits_dict['Apple']}")

# Modifying values (answering quiz question)
fruits_dict['Lemon'] = 0.75  # Change Lemon price
print(f"Updated Lemon price: ${fruits_dict['Lemon']}")

# Adding new key-value pairs
student['year'] = 'Sophomore'
fruits_dict['Grape'] = 2.00
print("\nAfter additions:")
print(f"Student: {student}")
print(f"Fruits: {fruits_dict}")

# Dictionary methods
print("\nDictionary methods:")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Safe access with get()
print(f"GPA: {student.get('gpa', 'Not found')}")
print(f"Graduation year: {student.get('graduation', 'Not specified')}")

# Checking for keys
print("\nKey existence:")
print(f"'name' in student: {'name' in student}")
print(f"'phone' in student: {'phone' in student}")
