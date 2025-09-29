# Example code from the module slides

condition = True

if condition:
    # Code to execute if condition is True
    print("This runs when condition is True")
print("Program continues...")

# Example: Age Check
age = 18
if age >= 18:
    print("You can vote!")

#Example: Temperature Check
temperature = 75 
if temperature > 70: 
    print("It's warm!")
else: 
    print("It's cool!")

# Example: Even/Odd
number = 7 
if number % 2 == 0: 
    print("Even") 
else: 
    print("Odd")


# elif
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# and - both conditions must be True
age = 25 
income = 50000 
if age >= 18 and income > 30000: 
    print("Eligible for loan")

day = "Sunday"
# or - at least one condition must be True
if day == "Saturday" or day == "Sunday": 
    print("It's weekend!")

# not reverses the condition
is_raining = False 
if not is_raining: 
    print("Go for a walk!")
    
weather = "sunny"
temperature = 75
if weather == "sunny": 
    print("It's a sunny day!") 
    if temperature > 80: 
        print("Perfect for swimming!") 
    elif temperature > 70: 
        print("Great for a picnic!") 
    else: 
        print("Nice for a walk!") 
else: 
    print("Maybe stay indoors")
    
    
    
# Get user input 
user_input = input("Enter your age: ") 

# Check if input is numeric 
if user_input.isdigit(): 
    age = int(user_input) 
    # Validate age range 
    if age < 0: 
        print("Age cannot be negative!") 
    elif age > 150: 
        print("That seems too old!") 
    else: 
        # Determine age category 
        if age < 13: 
            print("You're a child") 
        elif age < 20:
            print("You're a teenager")
        else:
            print("You're an adult")
else:
    print("Please enter a valid number!")
    

# Debug example
score = 85
print(f"Debug: score = {score}")

# Check the value
if score >= 90:
    # Track execution
    print("Debug: A branch")
    grade = "A"
elif score >= 80:
    # This should execute
    print("Debug: B branch")
    grade = "B"

print(f"Final grade: {grade}")
