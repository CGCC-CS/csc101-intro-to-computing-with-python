# This file has the example code from the module intro video
# Some variables have been defined so that the code runs without user input
# but in practice, you would get these values from input() calls.

x = 12 
y = 8

if x > 10 and y < 14:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")
    
aiSaleComplete = True
number = 32

if number==63 or aiSaleComplete:
    print("You get a discount!")
else:
    print("No discount for you.")


age = 30
if not age >= 35:
    print("You are not old enough to run for president.")
else:
    print("You are old enough to run for president.")