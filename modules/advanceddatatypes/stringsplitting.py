''' 
Demonstrates string splitting and joining methods in Python
'''

# Split method examples
sentence = "Python,Java,C++,JavaScript"
print(f"Original: {sentence}")
print(f"Split by comma: {sentence.split(',')}")

# Split with different delimiters
text = "apple-banana-cherry-date"
fruits = text.split('-')
print(f"Split by hyphen: {fruits}")

# Split with whitespace (default)
words = "The quick brown fox"
word_list = words.split()
print(f"Split by whitespace: {word_list}")

# Split with limit
data = "name:age:city:country:continent"
limited_split = data.split(':', 2)  # Split only first 2 occurrences
print(f"Limited split: {limited_split}")

# Join method - combining list into string
languages = ['Python', 'Java', 'C++', 'JavaScript']
joined = ', '.join(languages)
print(f"\nJoined with comma: {joined}")

# Join with different separators
joined_dash = '-'.join(languages)
print(f"Joined with dash: {joined_dash}")

# Join with space
joined_space = ' '.join(languages)
print(f"Joined with space: {joined_space}")
