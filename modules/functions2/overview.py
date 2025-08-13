"""
Functions 2 Overview - Advanced Python Function Concepts and Module Usage

This module demonstrates various advanced concepts in Python including:

1. Module Imports:
   - Basic imports (import math)
   - Multiple imports (import datetime, random)
   - Selective imports (from math import sin, pi)
   - Aliased imports (import math as m)

2. Built-in Module Usage:
   - Mathematical functions and constants from the math module
   - Date and time operations using datetime
   - Random number generation and choice selection

3. Advanced Function Features:
   - Functions with default parameters
   - Variable-length arguments (*args)
   - Keyword arguments (**kwargs)
   - Functions combining multiple parameter types

4. Variable Scope:
   - Global variables and the global keyword
   - Nested functions and the nonlocal keyword
   - Local vs enclosing vs global scope

5. Lambda Functions:
   - Anonymous functions using lambda expressions
   - Comparison with regular function definitions

This program serves as a comprehensive reference for students learning about
advanced function concepts and module usage in Python programming.

Author: Wade Huber
Date: August 12, 2025
"""

import math                  # Basic import
import datetime, random      # Multiple imports
from math import sin, pi     # Selective import
import math as m             # Aliased import

result = math.sqrt(16)
print("The square root of 16 is:", result)

# Using selective import for sin
print("The sine of pi/2 is:", sin(pi/ 2))

# Using aliased import for math
print("The cosine of pi is:", m.cos(m.pi))

# Cool stuff from math
# Constants
print("The value of pi is:", math.pi)
print("The value of e is:", math.e)

# Mathematical functions
print("The logarithm of 1000 to base 10 is:", math.log10(1000))
print("The logarithm of 1000 to base 2 is:", math.log2(1000))
print("The logarithm of 1000 to base e is:", math.log(1000))
print("The factorial of 5 is:", math.factorial(5))
print("The greatest common divisor of 48 and 64 is:", math.gcd(48, 64))

# Using datetime to get current date and time
current_time = datetime.datetime.now()
print("Current date and time:", current_time)

# Some examples using random
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random())
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))


# Function without default parameters
def greet1(name, greeting):
    """
    Create a greeting message using the provided name and greeting.
    
    Args:
        name (str): The name of the person to greet
        greeting (str): The greeting to use (e.g., "Hello", "Hi", "Good morning")
    
    Returns:
        str: A formatted greeting message
    """
    return f"{greeting}, {name}!"

# Function with default parameters
def greet(name, greeting="Hello"):
    """
    Create a greeting message with an optional greeting parameter.
    
    Args:
        name (str): The name of the person to greet
        greeting (str, optional): The greeting to use. Defaults to "Hello"
    
    Returns:
        str: A formatted greeting message
    """
    return f"{greeting}, {name}!"


# Function with variable-length arguments
def calculate_average(*numbers):
    """
    Calculate the average of a variable number of numeric arguments.
    
    Args:
        *numbers: Variable number of numeric values
    
    Returns:
        float: The arithmetic mean of all provided numbers
    
    Raises:
        ZeroDivisionError: If no numbers are provided
    """
    return sum(numbers) / len(numbers)

# Function with keyword arguments
def create_student(**details):
    """
    Display student information from keyword arguments.
    
    Args:
        **details: Arbitrary keyword arguments representing student details
                  (e.g., name="John", age=20, major="Computer Science")
    
    Returns:
        None: This function prints information and doesn't return a value
    """
    for key, value in details.items():
        print(f"{key}: {value}")

# Function with variable-length arguments, keyword arguments, and default parameters
def flexible_function(required, default="value", *args, **kwargs):
    """
    Demonstrate a function with all types of parameters.
    
    Args:
        required (any): A required positional argument
        default (str, optional): A parameter with a default value. Defaults to "value"
        *args: Variable number of additional positional arguments
        **kwargs: Arbitrary keyword arguments
    
    Returns:
        None: This function demonstrates parameter handling and doesn't return a value
    """
    print("Do some stuff")


# Scope
COUNTER = 0 # Global variable
def increment():
    """
    Increment the global COUNTER variable by 1.
    
    This function demonstrates the use of the global keyword to modify
    a global variable from within a function.
    
    Returns:
        None: This function modifies the global COUNTER and doesn't return a value
    """
    global COUNTER   # global keyword allows access to the global variable
    COUNTER += 1

def outer_function():
    """
    Demonstrate nested functions and the nonlocal keyword.
    
    This function contains an inner function that modifies a variable
    in the enclosing scope using the nonlocal keyword.
    
    Returns:
        int: The modified value of x (15)
    """
    x = 10

    def inner_function():
        nonlocal x  # nonlocal keyword allows access to the enclosing scope variable
        x += 5

    inner_function()
    return x

# lambdas
def square_function(x):
    """
    Calculate the square of a number using a regular function definition.
    
    This function demonstrates the traditional way to define a function
    and is compared with the lambda expression below.
    
    Args:
        x (numeric): The number to square
    
    Returns:
        numeric: The square of the input number (x²)
    """
    return x ** 2

square = lambda x: x ** 2
