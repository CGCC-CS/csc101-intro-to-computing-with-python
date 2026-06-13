"""Python error handling reference: try-except, raising, and best practices."""


# ============================================================
# Basic try-except Structure
# ============================================================
def divide(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"


print(divide(10, 2))   # 5.0
print(divide(10, 0))   # Error: Cannot divide by zero


# ============================================================
# Catching Multiple Exception Types
# ============================================================
def safe_convert_to_int(value):
    """Convert a value to integer with error handling."""
    try:
        return int(value)
    except ValueError:
        return f"Error: '{value}' cannot be converted to integer"
    except TypeError:
        return "Error: Invalid type for conversion"


print(safe_convert_to_int("42"))      # 42
print(safe_convert_to_int("hello"))   # Error: 'hello' cannot be converted...
print(safe_convert_to_int([1, 2]))    # Error: Invalid type for conversion


# ============================================================
# Using else and finally
# ============================================================
def read_file_safely(filename):
    """Read a file with comprehensive error handling."""
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        return "Error: File not found"
    except PermissionError:
        return "Error: Permission denied"
    else:
        # Executes only if no exception occurred
        print("File read successfully")
        return content
    finally:
        # Always executes; cleanup code
        if file is not None:
            file.close()
            print("File closed")


# ============================================================
# Raising Exceptions
# Functions can raise exceptions to signal errors to calling code.
# ============================================================
def calculate_grade(score):
    """Calculate letter grade with input validation."""
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    grade = "X"

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade


# Using the function
try:
    print(calculate_grade(95))      # A
    print(calculate_grade(150))     # raises ValueError
except ValueError as e:
    print(f"Invalid input: {e}")


# ============================================================
# Error Handling Best Practices
#   - Be specific: catch specific exceptions, not general Exception.
#   - Provide helpful messages: tell users what went wrong.
#   - Don't hide errors: log or report important errors.
#   - Validate inputs: check parameters at the start of functions.
#   - Use finally for cleanup: close files, connections, etc.
# ============================================================
def process_user_age(age_str):
    """Process and validate user age with clear error messages."""
    try:
        age = int(age_str)

        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")

        return age

    except ValueError as e:
        if "invalid literal" in str(e):
            return "Error: Please enter a valid number"
        else:
            return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
