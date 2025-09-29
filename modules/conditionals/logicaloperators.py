# Login system example
username = input("Enter username: ")
password = input("Enter password: ")

# Using 'and' operator
if username == "admin" and password == "12345":
    print("Login successful!")
else:
    print("Invalid credentials!")

# Using 'or' operator
day = input("Enter day of the week: ").lower()
if day == "saturday" or day == "sunday":
    print("It's weekend!")
else:
    print("It's a weekday.")

# Using 'not' operator
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"
if not is_raining:
    print("Good day for outdoor activities!")

# Complex logical expression
age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ").lower() == "yes"

if age >= 18 and has_license:
    print("You can rent a car!")
elif age >= 16 and has_license:
    print("You can drive but can't rent a car yet.")
else:
    print("You cannot drive.")
