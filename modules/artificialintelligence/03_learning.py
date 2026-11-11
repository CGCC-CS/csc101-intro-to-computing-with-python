# AI with Python Example 3: How a Model Learns
# CSC101 - Introduction to Computing with Python
# In Example 1 YOU tuned the model: change a number, check the errors,
# keep the change if it helped. This program gives the computer the same
# job. Guess, check, nudge, repeat. That loop is called TRAINING.

# ---------------------------------------------------------------
# Named constants
# ---------------------------------------------------------------
NUDGE = 0.01        # how far to move a parameter on each step
STEPS = 400         # how many times to repeat guess-check-nudge
REPORT_EVERY = 50   # print progress every 50 steps

miles = [1, 2, 3, 4, 5, 6, 8, 10]
fares = [4.40, 6.00, 8.10, 9.50, 11.70, 13.20, 17.00, 20.40]


def predict(distance, weight, bias):
    """Return the predicted fare (dollars) for a trip of the given distance."""
    return weight * distance + bias


def loss(weight, bias):
    """Return the mean squared error of the model over all the trips."""
    total = 0
    for i in range(len(miles)):
        error = predict(miles[i], weight, bias) - fares[i]
        total += error ** 2
    return total / len(miles)


# ---------------------------------------------------------------
# 1. Start with a bad guess
# ---------------------------------------------------------------
# The model starts out knowing nothing: every trip is predicted to be free.
weight = 0.0
bias = 0.0
print(f"Start: weight = {weight:.2f}, bias = {bias:.2f}, loss = {loss(weight, bias):.3f}")
print()

# ---------------------------------------------------------------
# 2. The training loop
# ---------------------------------------------------------------
losses = []   # save the loss at every step so we can look at it later

for step in range(1, STEPS + 1):
    # Nudge the weight. Try a little higher and a little lower,
    # and keep whichever one makes the loss smaller.
    if loss(weight + NUDGE, bias) < loss(weight, bias):
        weight += NUDGE
    elif loss(weight - NUDGE, bias) < loss(weight, bias):
        weight -= NUDGE

    # Nudge the bias the same way.
    if loss(weight, bias + NUDGE) < loss(weight, bias):
        bias += NUDGE
    elif loss(weight, bias - NUDGE) < loss(weight, bias):
        bias -= NUDGE

    losses.append(loss(weight, bias))

    if step % REPORT_EVERY == 0:
        print(f"Step {step:>3}: weight = {weight:.2f}, bias = {bias:.2f}, "
              f"loss = {losses[-1]:.3f}")

# ---------------------------------------------------------------
# 3. The trained model
# ---------------------------------------------------------------
print()
print(f"Learned model: fare = {weight:.2f} * miles + {bias:.2f}")
print(f"Predicted fare for 7 miles: ${predict(7, weight, bias):.2f}")

# Nobody typed in a cost per mile or a starting fee. The program found
# them from the data. That is what "machine learning" means.

# ---------------------------------------------------------------
# How this connects to PyTorch (Example 5)
# ---------------------------------------------------------------
#   This program                    PyTorch
#   ------------------------------  ------------------------------
#   weight, bias                    model.parameters()
#   predict()                       model(inputs)
#   loss()                          criterion (the loss function)
#   NUDGE                           lr (the learning rate)
#   one pass through the loop       one epoch
#   the two if/elif blocks          loss.backward() + optimizer.step()
#
# PyTorch does not try "higher" and "lower" for every parameter. It uses
# calculus to work out the best direction for all of them at once, which
# is why it can train models with millions of parameters.

# TRY IT:
# 1. Change NUDGE to 0.5. What happens to the final loss, and why?
# 2. Change NUDGE to 0.001. How many STEPS does it need now?
# 3. The loss drops quickly at first and then levels off. Print the
#    losses list (or plot it with Matplotlib) to see the shape.
