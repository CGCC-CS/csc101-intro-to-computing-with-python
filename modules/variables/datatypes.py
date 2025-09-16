"""
This program demonstrates various data types in Python with examples.

Author: Wade Huber
Date: August 23, 2025
"""

age = 21              # integer
pi = 3.14159          # floating point
name = "Kendra"       # string
is_student = True     # boolean
imaginary = 3 + 4j    # complex

grades = [85, 92, 78] # list
coordinates = (3, 4)  # tuple
student_info = {"name": "Seth", "age": 11}  # dict
unique_ids = {101, 102, 103}  # set

# Print each variable with its value and type for demonstration
print(f"Age: {age}, Type: {type(age)}")
print(f"Price: {pi}, Type: {type(pi)}")  # Added formatting for currency
print(f"Name: '{name}', Type: {type(name)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")
print(f"Complex: {imaginary}, Type: {type(imaginary)}")

print(f"Grades: {grades}, Type: {type(grades)}")
print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")
print(f"Student Info: {student_info}, Type: {type(student_info)}")
print(f"Unique IDs: {unique_ids}, Type: {type(unique_ids)}")


name = 42
grades = 'This is a grade'

print(f"Name: '{name}', Type: {type(name)}")
print(f"Grades: {grades}, Type: {type(grades)}")
