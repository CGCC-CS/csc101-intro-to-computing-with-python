# Docstrings

# Use triple quotes (""") to create a docstring:
def function_name(parameters):
    """Brief description of what the function does."""
    # Function code

def greet(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")

def calculate_area(length, width):
    """Calculate and return the area of a rectangle."""
    return length * width

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

# Multi-line Docstrings
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    The formula used is: F = (C × 9/5) + 32
    """
    return (celsius * 9/5) + 32

# Docstring conventions for Parameters and Return Values
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    BMI is calculated as weight in kilograms divided by 
    height in meters squared.
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: The calculated BMI value
    """
    return weight / (height ** 2)

# Examples of Well-Documented Functions

# Example 1: Grade Calculator
def calculate_final_grade(midterm, final, homework):
    """
    Calculate final course grade based on weighted components.
    
    The final grade is calculated as:
    - Midterm: 30%
    - Final exam: 40%
    - Homework: 30%
    
    Args:
        midterm (float): Midterm exam score (0-100)
        final (float): Final exam score (0-100)
        homework (float): Homework average score (0-100)
    
    Returns:
        float: Final grade percentage (0-100)
    """
    return (midterm * 0.3) + (final * 0.4) + (homework * 0.3)

# Example 2: Shopping Cart
def add_to_cart(cart, item, price, quantity=1):
    """
    Add an item to the shopping cart.
    
    If the item already exists in the cart, the quantity
    is increased. Otherwise, a new entry is created.
    
    Args:
        cart (dict): Shopping cart dictionary
        item (str): Name of the item
        price (float): Price per unit
        quantity (int): Number of items (default: 1)
    
    Returns:
        dict: Updated shopping cart
    """
    if item in cart:
        cart[item]['quantity'] += quantity
    else:
        cart[item] = {'price': price, 'quantity': quantity}
    
    return cart

# Example 3: Temperature Analyzer
def analyze_temperatures(temps):
    """
    Analyze a list of temperature readings.
    
    Args:
        temps (list): List of temperature values (floats)
    
    Returns:
        dict: Dictionary containing:
            - 'min': Minimum temperature
            - 'max': Maximum temperature
            - 'avg': Average temperature
            - 'count': Number of readings
    """
    return {
        'min': min(temps),
        'max': max(temps),
        'avg': sum(temps) / len(temps),
        'count': len(temps)
    }

# You can view docstrings using Python's built-in help() function:
def square(x):
    """Return the square of x."""
    return x * x

# View the docstring
help(square)
