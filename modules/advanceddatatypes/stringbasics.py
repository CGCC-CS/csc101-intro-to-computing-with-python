''' 
Demonstrates string creation, indexing, and basic methods
'''

# String creation and quoting
single_quote = 'Hello World'
double_quote = "It's a nice day"  # Contains single quote
escaped_quote = "It\'s also fine"  # Escaped single quote
multi_line = """This is a
multi-line string"""

print("String examples:")
print(single_quote)
print(double_quote)
print(escaped_quote)

# String length and indexing
greeting = 'How are you?'
print(f"\nString: '{greeting}'")
print(f"Length: {len(greeting)}")
print(f"First character: {greeting[0]}")
print(f"Last character: {greeting[-1]}")

# Finding characters and substrings
text = "Python Programming"
print(f"\nSearching in '{text}':")
print(f"First 'o' at index: {text.find('o')}")
print(f"First 'Python' at index: {text.find('Python')}")
print(f"'Java' found: {text.find('Java')}")  # Returns -1 if not found
