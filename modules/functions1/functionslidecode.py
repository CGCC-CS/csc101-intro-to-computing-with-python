# Code from the slides for the Functions module

import math

# Without functions - repetitive 
area1 = 5 * 3 
area2 = 7 * 4 

# With functions - reusable 

# length and width are parameters
def calculate_area(length, width): 
      return length * width
 
result = "Gotta define something so that the example below works!" 

def function_name(parameters): 
    """Docstring: describes what function does"""
    # Function body 
    # Code to execute 
    return result

def greet(): 
    """Print a welcome message"""
    print("Welcome to CSC101!") 
    print("Let's learn about functions!")

# Call the function 
greet()


numbers = [10, 25, 5, 30]
print(f"Length: {len(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")




radius = 5
area = math.pi * radius ** 2
print(f"Area: {area}")

def greet(name):        # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")          # "Alice" is an argument

calculate_area(5, 3)    # 5 and 3 are arguments

def introduce(name, age, city):
    print(f"{name} is {age} years old")
    print(f"Lives in {city}")

# Correct order
introduce("Alice", 25, "Phoenix")

# Wrong order = wrong output!
introduce(25, "Alice", "Phoenix")
# Output: 25 is Alice years old

def describe_pet(animal, name, age):
    print(f"{name} is a {age}-year-old {animal}")

# Using parameter names
describe_pet(name="Rex", age=3, animal="dog")
describe_pet(age=3, animal="dog", name="Rex")

# Both produce same output:
# Rex is a 3-year-old dog

def book_trip(destination, duration, travelers):
    print(f"{duration} days in {destination}")
    print(f"for {travelers} people")

# Correct
book_trip("Paris", duration=5, travelers=2)

# Error: keyword before positional
book_trip(destination="Paris", 5, 2)

def custom_greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Use default
custom_greet("Alice")           # Hello, Alice!

# Override default
custom_greet("Bob", "Hi")       # Hi, Bob!
custom_greet("Charlie", greeting="Hey")  # Hey, Charlie!


def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

# Output: 25°C = 77.0°F

def get_stats(numbers):
    """Return min, max, and average"""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

data = [10, 25, 30, 15, 20]
min_val, max_val, avg_val = get_stats(data)

print(f"Min: {min_val}")
print(f"Max: {max_val}")
print(f"Average: {avg_val}")


def get_factors(number):
    """Return all factors of a number"""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

result = get_factors(12)
print(f"Factors of 12: {result}")
# Output: Factors of 12: [1, 2, 3, 4, 6, 12]

def analyze_text(text):
    """Analyze text and return statistics"""
    stats = {
        'length': len(text),
        'words': len(text.split()),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower())
    }
    return stats

sample = "Hello World"
results = analyze_text(sample)

print(f"Length: {results['length']}")
print(f"Words: {results['words']}")


def calculate_bmi(weight, height):
    """Calculate Body Mass Index"""
    return weight / (height ** 2)

def calculate_bmi_documented(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: The calculated BMI value
    """
    return weight / (height ** 2)


def calculate(x, y):
    result = x + y    # result is LOCAL
    return result

# result doesn't exist here!
# print(result)  # NameError!

answer = calculate(5, 3)
print(answer)  # 8