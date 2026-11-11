# Module 13 Example 4: Matplotlib Basics
# CSC101 - Introduction to Computing with Python
# Builds four kinds of charts: a line plot with a reference line,
# a bar plot, a scatter plot, and a histogram.

import numpy as np
import matplotlib.pyplot as plt  # "plt" is the standard alias for pyplot

# ---------------------------------------------------------------
# Chart 1: Line plot of two models on the same graph
# ---------------------------------------------------------------
# Line plots show how something changes over time.
PEAK_HOUR = 15
HOT_TEMP = 100

hours = np.linspace(6, 21, 151)
summer_temps = -0.5 * (hours - PEAK_HOUR) ** 2 + 108   # a July day
spring_temps = -0.5 * (hours - PEAK_HOUR) ** 2 + 88    # an April day

plt.figure()  # start a new, empty chart

# Each plt.plot() call adds one line. The label is used by the legend.
plt.plot(hours, summer_temps, label="July: high 108 F")
plt.plot(hours, spring_temps, label="April: high 88 F")

# A dashed horizontal reference line at 100 degrees.
plt.axhline(HOT_TEMP, color="red", linestyle="--", label="100 F")

# Every graph needs a title and axis labels so readers know what it shows.
plt.title("Modeled Temperature in Chandler")
plt.xlabel("Hour of the day (24-hour clock)")
plt.ylabel("Temperature (F)")
plt.grid(True)    # light background grid makes values easier to read
plt.legend()      # shows the label for each line

# ---------------------------------------------------------------
# Chart 2: Bar plot to compare categories
# ---------------------------------------------------------------
months = ["Jan", "Apr", "Jul", "Oct"]
rain = [0.9, 0.3, 1.1, 0.6]

plt.figure()
plt.bar(months, rain, color="teal")
plt.title("Average Rain in Chandler")
plt.xlabel("Month")
plt.ylabel("Rain (inches)")

# ---------------------------------------------------------------
# Chart 3: Scatter plot to show a relationship
# ---------------------------------------------------------------
# Does studying more go with higher quiz scores? Each dot is one student.
study_hours = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
quiz_scores = [55, 62, 58, 70, 74, 80, 77, 85, 88, 94]

plt.figure()
plt.scatter(study_hours, quiz_scores)
plt.title("Study Time and Quiz Scores")
plt.xlabel("Hours studied")
plt.ylabel("Quiz score")
plt.grid(True)

# ---------------------------------------------------------------
# Chart 4: Histogram to show a distribution
# ---------------------------------------------------------------
# A histogram groups values into "bins" and counts how many land in each.
exam_scores = [52, 61, 64, 68, 70, 72, 73, 75, 77, 78,
               80, 81, 83, 84, 85, 86, 88, 90, 93, 97]

plt.figure()
plt.hist(exam_scores, bins=5, edgecolor="black")
plt.title("Distribution of Exam Scores")
plt.xlabel("Score")
plt.ylabel("Number of students")

# ---------------------------------------------------------------
# Show every chart
# ---------------------------------------------------------------
# plt.show() goes LAST. In VS Code, the program pauses here until you
# close the chart windows. In Colab, charts appear below the cell.
print("Showing 4 charts. Close the windows to end the program.")
plt.show()
