'''
Examples of working with strings in Python
    creation, indexing, iteration, and common methods
'''

LIST = ['W', 'o', 'r', 'l', 'd']      # List of characters
print(f"list = {LIST} length={len(LIST)}")

STR1 = "Hello"
STR2 = "".join(['e', 'n', 'd', '.'])  # Create a list by joining a list of characters together
STR3 = "This is a really long string.  Maybe too long?"

print(f"str1 = {STR1} length={len(STR1)}")
print(f"str2 = {STR2} length={len(STR2)}")
print(f"str3 = {STR3} length={len(STR3)}")

print("String 1 character by character: ")
for char in STR1:
    print(f"  {char}")

print("String 2 ASCII values: ")
for char in STR1:
    print(f"  {char} (ASCII={ord(char)})")

#appending a string
STR5 = STR1 + " " + "".join(STR2) + "!"
print(STR5)

# more string functions
print(STR3.upper())
print(STR3.lower())
