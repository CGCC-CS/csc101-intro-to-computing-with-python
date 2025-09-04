"""
This program contains the code examples from the module intro video
"""

# Numbers
age = 25 # int
price = 19.99 # float
pi = 3.14159 # float

# Text & Logic
name = "Python" # str
is_fun = True # bool
is_hard = False # bool

# Collections
colors = ["red", "blue"] # list
point = (10, 20) # tuple
person = {"name": "Alice"} # dict

# Variable Assignment
student_name = "Alice"
test_score = 95
grade_average = 87.5

# Arithmetic Operators
total = 10 + 5      # Addition
result = 20 * 3     # Multiplication
average = total / 4 # Division

gpa = 3.4
score = 100
credits = 130

# Comparison & Logic
is_passing = score >= 70
grade = gpa > 3.0 and credits >= 120
needs_help = not is_passing

# Getting User Input
name = input("Enter your name: ")
age = int(input("Enter age: "))
gpa = float(input("Enter GPA: "))

# Displaying Output
print("Hello", name)
print(f"You are {age} years old")
print("GPA: {:.2f}".format(gpa))

# Comments & Documentation
exam1 = 94
exam2 = 87

"""
This program calculates student grades
Author: Tony Stark
"""

# Calculate the final grade
final_grade = (exam1 + exam2) / 2
