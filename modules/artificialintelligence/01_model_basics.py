# AI with Python Example 1: A Model Is a Function
# CSC101 - Introduction to Computing with Python
# A "model" sounds mysterious, but it is just a function with a few
# adjustable numbers inside it. This program builds a tiny model that
# predicts the cost of a ride-share trip, and you tune it by hand.

# ---------------------------------------------------------------
# 1. The data: trips we already know the answer for
# ---------------------------------------------------------------
# Each position lines up: the 1-mile trip cost $4.40, the 2-mile trip
# cost $6.00, and so on. Data with known answers is called TRAINING DATA.
miles = [1, 2, 3, 4, 5, 6, 8, 10]
fares = [4.40, 6.00, 8.10, 9.50, 11.70, 13.20, 17.00, 20.40]


# ---------------------------------------------------------------
# 2. The model: a function with two adjustable numbers
# ---------------------------------------------------------------
def predict(distance, weight, bias):
    """Return the predicted fare (dollars) for a trip of the given distance.

    weight is the cost per mile. bias is the starting fee you pay
    before the car moves. These two numbers are the model's PARAMETERS.
    """
    return weight * distance + bias


# ---------------------------------------------------------------
# 3. Make a guess for the parameters
# ---------------------------------------------------------------
# CHANGE THESE two numbers, run the program again, and watch the
# predictions get better or worse. That is all "training" is.
weight = 1.00   # dollars per mile
bias = 1.00     # starting fee in dollars

# ---------------------------------------------------------------
# 4. Compare the model's predictions to the real answers
# ---------------------------------------------------------------
print(f"Model: fare = {weight:.2f} * miles + {bias:.2f}")
print()
print(f"{'Miles':>5}{'Actual':>10}{'Predicted':>12}{'Error':>9}")
print("-" * 36)

# range(len(miles)) gives the indexes 0, 1, 2, ... so we can read
# the same position from both lists.
for i in range(len(miles)):
    predicted = predict(miles[i], weight, bias)
    error = predicted - fares[i]   # negative = guessed too low
    print(f"{miles[i]:>5}{fares[i]:>10.2f}{predicted:>12.2f}{error:>9.2f}")

# ---------------------------------------------------------------
# 5. Use the model on a trip it has never seen
# ---------------------------------------------------------------
# There is no 7-mile trip in the data. A model is useful because it can
# make a prediction for NEW inputs, not just repeat the answers it was given.
new_trip = 7
print()
print(f"Predicted fare for {new_trip} miles: ${predict(new_trip, weight, bias):.2f}")

# TRY IT:
# 1. Every error starts out negative. What does that tell you about weight?
# 2. Change weight and bias until every error is between -0.50 and 0.50.
# 3. How did you decide which number to change, and in which direction?
#    Example 3 teaches the computer to make that same decision.
