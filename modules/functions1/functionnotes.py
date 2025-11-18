
import math

print("Program starts") 

def greet():             # Function definition
    print("Hello!")

    
greet()


def welcome_message():
    """Prints a welcome message to the user"""
    print("Welcome to CSC101!")
    print("Let's learn about functions!")

# Call the function
welcome_message()

def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    area = length * width
    print(f"Area: {area}")

calculate_area(5, 3)
calculate_area(7, 4)

# input() - Gets user input as a string
name = input("Enter your name: ")

# print() - Displays output
print("Hello,", name)

# int() - Converts to integer
age = int(input("Enter age: "))

# float() - Converts to decimal number
price = float(input("Enter price: "))

# str() - Converts to string
number = 42
text = str(number)  # "42"

# range() - Generate sequence of numbers
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# List functions
# len() - Length of a sequence
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

# sorted() - Returns sorted version
numbers = [5, 2, 8, 1, 9]
print(sorted(numbers))  # Output: [1, 2, 5, 8, 9]

# type() - Returns the type of an object
x = 42
print(type(x))  # Output: <class 'int'>


# Built in math functions
# abs() - Absolute value
print(abs(-5))      # Output: 5

# round() - Round to nearest integer
print(round(3.7))   # Output: 4
print(round(3.14159, 2))  # Output: 3.14

# max() - Largest value
print(max(10, 25, 5))  # Output: 25

# min() - Smallest value
print(min(10, 25, 5))  # Output: 5

# sum() - Sum of a sequence
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15

# Using math module functions
# Square root
print(math.sqrt(25))      # Output: 5.0

# Power
print(math.pow(2, 3))     # Output: 8.0

# Constants
print(math.pi)            # Output: 3.141592653589793
print(math.e)             # Output: 2.718281828459045

# Trigonometric functions
print(math.sin(math.pi/2))  # Output: 1.0
print(math.cos(0))          # Output: 1.0

# Logarithms
print(math.log(10))       # Natural log
print(math.log10(100))    # Output: 2.0


def greet_person(name):        # 'name' is a parameter
    print(f"Hello, {name}!")

greet_person("Alice")          # "Alice" is an argument

def square(number):
    """Calculate the square of a number"""
    result = number * number
    print(result)

square(5)   # Output: 25
square(10)  # Output: 100

# Multiple parameters
def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    area = length * width
    print(f"Area: {area}")

calculate_area(5, 3)   # Output: Area: 15
calculate_area(7, 4)   # Output: Area: 28

def introduce(name, age, city):
    """Introduce a person"""
    print(f"{name} is {age} years old and lives in {city}")

introduce("Alice", 25, "Phoenix")  # Correct order
# Output: Alice is 25 years old and lives in Phoenix

introduce(25, "Alice", "Phoenix")  # Wrong order!
# Output: 25 is Alice years old and lives in Phoenix (incorrect!)

# The number and order of arguments must match the parameters!
def divide(numerator, denominator):
    result = numerator / denominator
    print(result)

divide(10, 2)   # Output: 5.0
divide(2, 10)   # Output: 0.2 (different result!)

def describe_pet(animal, name, age):
    """Describe a pet"""
    print(f"{name} is a {age}-year-old {animal}")

# Using positional arguments (order matters)
describe_pet("dog", "Rex", 3)

# Using keyword arguments (order doesn't matter)
describe_pet(name="Rex", age=3, animal="dog")
describe_pet(age=3, animal="dog", name="Rex")  # Same result!

def book_trip(destination, duration, travelers):
    print(f"Booking {duration} days in {destination} for {travelers} people")

# Correct: Positional first, then keyword
book_trip("Paris", duration=5, travelers=2)

# Error: Keyword before positional
# book_trip(destination="Paris", 5, 2)  # SyntaxError!


# Default parameters
def greet(name, greeting="Hello"):
    """Greet someone with a customizable greeting"""
    print(f"{greeting}, {name}!")

# Using default greeting
greet("Alice")              # Output: Hello, Alice!

# Providing custom greeting
greet("Bob", "Hi")          # Output: Hi, Bob!
greet("Charlie", greeting="Hey")  # Output: Hey, Charlie!

def create_account(username, email, role="user", active=True):
    """Create a user account with optional parameters"""
    print("Account created:")
    print(f"  Username: {username}")
    print(f"  Email: {email}")
    print(f"  Role: {role}")
    print(f"  Active: {active}")

# Only required parameters
create_account("alice123", "alice@email.com")

# Some optional parameters
create_account("bob456", "bob@email.com", role="admin")

# All parameters specified
create_account("charlie", "charlie@email.com", "moderator", False)

# Returning values from functions
def add(a, b):
    """Add two numbers and return the result"""
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# If no return statement is used, functions return None by default
def print_greeting(name):
    print(f"Greetings, {name}!")

result = greet("Alice")  # Prints: Hello, Alice!
print(result)            # Output: None

# return statements immediately exit the function
def check_age(age):
    """Check if someone is old enough to vote"""
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible yet"

print(check_age(20))  # Output: Eligible to vote
print(check_age(15))  # Output: Not eligible yet

# Functions can return any data type.
def get_grade(score):
    """Convert numeric score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

grade = get_grade(85)
print(f"Your grade is: {grade}")  # Output: Your grade is: B

# Using Return Values in Expressions
def square(x):
    return x * x

def cube(x):
    return x * x * x

# Use return values in calculations
result = square(5) + cube(2)  # 25 + 8 = 33
print(result)  # Output: 33

# Use in conditions
if square(4) > 10:
    print("Square of 4 is greater than 10")

# Example 1: Calculate Tax
def calculate_tax(amount, tax_rate=0.08):
    """Calculate tax on a purchase"""
    return amount * tax_rate

subtotal = 100
tax = calculate_tax(subtotal)
total = subtotal + tax
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")

# Example 2: Temperature Conversion
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")  # Output: 25°C = 77.0°F

# Example 3: Days Alive Calculator
def days_alive(age):
    """Calculate approximate days alive based on age"""
    days = age * 365.24
    return round(days)

user_age = int(input("Enter your age: "))
days = days_alive(user_age)
print(f"You have been alive about {days} days.")

# You can use the return value of one function as an argument to another.
def double(x):
    return x * 2

# Use return value of double() as argument to square()
result = square(double(3))  # square(6) = 36
print(result)  # Output: 36

# Multiple Function Outputs

# Tuple Return
def get_name():
    """Return first and last name"""
    first = "Alice"
    last = "Smith"
    return first, last  # Returns a tuple

# Unpack the tuple
first_name, last_name = get_name()
print(f"First: {first_name}, Last: {last_name}")
# Output: First: Alice, Last: Smith

# Multiple Statistics Example
def calculate_stats(numbers):
    """Calculate min, max, and average of a list"""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

data = [10, 25, 30, 15, 20]
min_val, max_val, avg_val = calculate_stats(data)

print(f"Min: {min_val}")
print(f"Max: {max_val}")
print(f"Average: {avg_val}")

# Coordinate Example
def get_coordinates():
    """Return x and y coordinates"""
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    return x, y

# Use the coordinates
x_pos, y_pos = get_coordinates()
print(f"Position: ({x_pos}, {y_pos})")

# Returning Lists
def get_factors(number):
    """Return all factors of a number as a list"""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

result = get_factors(12)
print(f"Factors of 12: {result}")
# Output: Factors of 12: [1, 2, 3, 4, 6, 12]

# Filtering Example
def split_scores(scores):
    """Split scores into passing and failing"""
    passing = []
    failing = []
    
    for score in scores:
        if score >= 60:
            passing.append(score)
        else:
            failing.append(score)
    
    return passing, failing

all_scores = [85, 45, 92, 58, 73, 67, 55]
pass_list, fail_list = split_scores(all_scores)

print(f"Passing: {pass_list}")
print(f"Failing: {fail_list}")

# Returning Dictionaries
def analyze_text(text):
    """Analyze text and return statistics"""
    stats = {
        'length': len(text),
        'words': len(text.split()),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower())
    }
    return stats

sample = "Hello World! This is Python."
results = analyze_text(sample)

print(f"Length: {results['length']}")
print(f"Words: {results['words']}")
print(f"Uppercase: {results['uppercase']}")
print(f"Lowercase: {results['lowercase']}")

# Student Information Example
def create_student(name, age, major, gpa):
    """Create a student record as a dictionary"""
    student = {
        'name': name,
        'age': age,
        'major': major,
        'gpa': gpa,
        'status': 'active'
    }
    return student

student1 = create_student("Alice", 20, "Computer Science", 3.8)
print(student1)
# Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 
#          'gpa': 3.8, 'status': 'active'}

print("Program ends")
