''' 
Demonstrates common string methods in Python
'''

text = "  Python Programming Language  "
print(f"Original: '{text}'")

# Case conversion
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Title: '{text.title()}'")
print(f"Capitalize: '{text.capitalize()}'")

# Whitespace handling
print(f"Strip: '{text.strip()}'")
print(f"Left strip: '{text.lstrip()}'")
print(f"Right strip: '{text.rstrip()}'")

# String testing methods
print("\nString tests:")
print(f"Is alphabetic: {'Python'.isalpha()}")
print(f"Is numeric: {'123'.isnumeric()}")
print(f"Is alphanumeric: {'Python3'.isalnum()}")

# Replace and formatting
sentence = "I love Java programming"
print(f"\nOriginal: {sentence}")
print(f"Replaced: {sentence.replace('Java', 'Python')}")
