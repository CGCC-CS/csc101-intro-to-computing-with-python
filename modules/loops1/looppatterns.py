
# Basic While Loop Patterns

# Counting - count from 1 to 5
counter = 1
while counter <= 5:
    print(counter)
    counter += 1  # Important: modify the counter!

# You don't have to count up by 1, you can count down or by other increments
# Counting down from 12 by 2's
counter = 12
while counter >= 0: # note the direction of the inequality
    print(counter)
    counter -= 2  # Decrement the counter by 2 each time

# Sum numbers from 1 to 5 using a counting loop
total = 0
counter = 1
while counter <= 5:
    print(f"Adding: {counter}")
    total += counter
    counter += 1
print(f"The sum of numbers from 1 to 5 is: {total}")


# Input Validation - Keep asking until valid input
response = ""
print("Do you want to continue? (yes/no): ")
while response != "yes" and response != "no":
    response = input("Please enter 'yes' or 'no': ")
print(f"You chose: {response.lower()}")

# This loop ensures the user enters a grade between 0 and 100
grade = -1
while grade < 0 or grade > 100:
    grade = int(input("Enter a grade (0-100): "))
    if grade < 0 or grade > 100:
        print("Error: Grade must be between 0 and 100.")
print(f"Valid grade entered: {grade}")

# Sentinel-Controlled Loop - A loop that continues until a specific value
#    (sentinel) is encountered
# This loop processes numbers until -1 is entered
number = int(input("Enter a number (-1 to stop): "))
total = 0
while number != -1:
    print(f"You entered: {number}")
    total += number
    number = int(input("Enter a number (-1 to stop): "))
print(f"Total sum of entered numbers: {total}")

# Infinite loop with break (use sparingly)
# This loop will run indefinitely until 'exit' is entered
while True:
    user_input = input("Enter command: ")
    if user_input == "exit":
        break
    print(f"Processing: {user_input}")

