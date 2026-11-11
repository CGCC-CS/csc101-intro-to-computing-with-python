# Module 13 Example 1: NumPy Basics
# CSC101 - Introduction to Computing with Python
# Shows how to create NumPy arrays and do math on a whole array at once.

import numpy as np  # "np" is the standard nickname (alias) for NumPy

# ---------------------------------------------------------------
# 1. Create an array from a list
# ---------------------------------------------------------------
# A NumPy array looks like a list, but every value has the same type
# and you can do math on all of the values at once.
quiz_scores = np.array([78, 85, 92, 64, 88])

print("Quiz scores:", quiz_scores)
print("Number of scores (.size):", quiz_scores.size)
print("First score:", quiz_scores[0])        # indexing works like a list
print("First three scores:", quiz_scores[:3])  # slicing works like a list

# ---------------------------------------------------------------
# 2. Math on every element at once (no loop needed)
# ---------------------------------------------------------------
# With a regular list, adding 5 to every score needs a loop:
score_list = [78, 85, 92, 64, 88]
curved_list = []
for score in score_list:
    curved_list.append(score + 5)
print("\nCurved with a loop:  ", curved_list)

# With a NumPy array, one line does the same thing:
curved_scores = quiz_scores + 5
print("Curved with NumPy:   ", curved_scores)

# Every math operator works this way: +, -, *, /, **
percent_scores = quiz_scores / 100
print("As decimals:         ", percent_scores)

# Watch out: + means something different for lists!
print("\nList + list joins them:  ", [1, 2] + [3, 4])
print("Array + array adds them: ", np.array([1, 2]) + np.array([3, 4]))

# ---------------------------------------------------------------
# 3. Built-in statistics
# ---------------------------------------------------------------
print("\nLowest score: ", np.min(quiz_scores))
print("Highest score:", np.max(quiz_scores))
print("Average score:", np.mean(quiz_scores))
print("Total points: ", np.sum(quiz_scores))

# ---------------------------------------------------------------
# 4. Ready-made arrays: arange and linspace
# ---------------------------------------------------------------
# np.arange(start, stop, step) works like range(), and stop is NOT included.
evens = np.arange(0, 11, 2)
print("\nnp.arange(0, 11, 2):   ", evens)

# np.linspace(start, stop, count) makes "count" evenly spaced values,
# and stop IS included. Great for time values.
five_steps = np.linspace(0, 1, 5)
print("np.linspace(0, 1, 5):  ", five_steps)
