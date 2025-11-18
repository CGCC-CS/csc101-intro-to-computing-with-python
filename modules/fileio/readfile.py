# Open and read a file, printing its contents
# Without error handling!
file = open("data.txt", 'r')
content = file.read()
print(content)
file.close()
