# Open and read a file, printing its contents
# Without error handling!
with open("data.txt", "r") as file:
    content = file.read()
# File is closed here automatically
print(content)
