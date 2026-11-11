# AI with Python Example 2: Measuring How Wrong a Model Is (Loss)
# CSC101 - Introduction to Computing with Python
# In Example 1 you looked at a table of errors to judge the model.
# A computer needs ONE number instead. That number is called the LOSS:
# the bigger the loss, the worse the model. Zero would be a perfect model.

miles = [1, 2, 3, 4, 5, 6, 8, 10]
fares = [4.40, 6.00, 8.10, 9.50, 11.70, 13.20, 17.00, 20.40]


def predict(distance, weight, bias):
    """Return the predicted fare (dollars) for a trip of the given distance."""
    return weight * distance + bias


# ---------------------------------------------------------------
# 1. Why not just add up the errors?
# ---------------------------------------------------------------
# One guess is $3 too high and another is $3 too low. Added together the
# errors cancel out to 0, which looks perfect even though both are wrong.
errors = [3.00, -3.00]
print("Sum of errors:", sum(errors))

# Squaring fixes this. A squared number is never negative, and big
# mistakes count much more than small ones (3 squared is 9, 1 squared is 1).
squared_errors = [error ** 2 for error in errors]
print("Sum of squared errors:", sum(squared_errors))
print()


# ---------------------------------------------------------------
# 2. The loss function: mean squared error
# ---------------------------------------------------------------
def loss(weight, bias):
    """Return the mean squared error of the model over all the trips.

    Uses the accumulator pattern: start a total at 0, add the squared
    error for each trip, then divide by the number of trips.
    """
    total = 0
    for i in range(len(miles)):
        error = predict(miles[i], weight, bias) - fares[i]
        total += error ** 2
    return total / len(miles)


# ---------------------------------------------------------------
# 3. Use the loss to compare models
# ---------------------------------------------------------------
# Each tuple is one guess for (weight, bias). The loss tells us which
# guess is best without reading a whole table of errors.
guesses = [(1.00, 1.00), (2.00, 0.00), (1.50, 3.00), (1.80, 2.50)]

print(f"{'Weight':>6}{'Bias':>8}{'Loss':>10}")
print("-" * 24)
for weight, bias in guesses:
    print(f"{weight:>6.2f}{bias:>8.2f}{loss(weight, bias):>10.3f}")

# ---------------------------------------------------------------
# 4. Find the best guess with a loop
# ---------------------------------------------------------------
# Same "find the smallest" pattern you have used on lists of numbers.
best_guess = guesses[0]
for guess in guesses:
    if loss(guess[0], guess[1]) < loss(best_guess[0], best_guess[1]):
        best_guess = guess

print()
print(f"Best guess: weight = {best_guess[0]:.2f}, bias = {best_guess[1]:.2f}")

# TRY IT:
# 1. Add your best weight and bias from Example 1 to the guesses list.
#    Did you beat the best guess in the table?
# 2. Why can the loss never be negative?
# 3. The data is real-world messy, so no straight line fits it perfectly.
#    What does that mean for the lowest loss you can reach?
