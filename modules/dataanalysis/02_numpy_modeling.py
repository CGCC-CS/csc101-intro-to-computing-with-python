# Module 13 Example 2: Modeling with NumPy
# CSC101 - Introduction to Computing with Python
# Models the temperature during a hot summer day in Chandler and uses
# NumPy to answer questions about it: highest temperature, when it happens,
# when it first reaches 100 degrees, and how many hours it stays above 100.

import numpy as np

# ---------------------------------------------------------------
# Named constants: every fixed value gets a name
# ---------------------------------------------------------------
START_HOUR = 6       # 6:00 AM (hours on a 24-hour clock)
END_HOUR = 21        # 9:00 PM
NUM_POINTS = 151     # number of time values
TIME_STEP = 0.1      # hours between time values (6.0, 6.1, 6.2, ...)
PEAK_HOUR = 15       # hottest time of day: 3:00 PM
HIGH_TEMP = 108      # the day's high temperature (degrees F)
CHECK_HOUR = 12      # time for the temperature check (noon)
HOT_TEMP = 100       # "triple digits" (degrees F)


def temperature(hour):
    """Return the modeled temperature (degrees F) at the given hour.

    hour can be a single number OR a whole NumPy array. Because NumPy
    does math on every element, this function needs no loop.
    """
    return -0.5 * (hour - PEAK_HOUR) ** 2 + HIGH_TEMP


# ---------------------------------------------------------------
# 1. Build the time and temperature arrays
# ---------------------------------------------------------------
# linspace makes 151 evenly spaced values from 6 to 21, including both ends.
# (21 - 6) / 150 = 0.1, so the values are 0.1 hours apart.
hours = np.linspace(START_HOUR, END_HOUR, NUM_POINTS)

# Call the function ONCE with the whole array: 151 temperatures, no loop.
temps = temperature(hours)

print("Time points:", hours.size)
print("First 3 hours:", hours[:3])
print("First 3 temps:", temps[:3])

# ---------------------------------------------------------------
# 2. The same function works on a single number
# ---------------------------------------------------------------
noon_temp = temperature(CHECK_HOUR)

# ---------------------------------------------------------------
# 3. Find the highest value with np.argmax()
# ---------------------------------------------------------------
# np.max() tells you the highest temperature, but not WHEN it happened.
# np.argmax() gives the INDEX (position) of the highest value.
# Use that one index to look up the value in BOTH arrays.
peak_index = np.argmax(temps)
peak_temp = temps[peak_index]
peak_time = hours[peak_index]

# ---------------------------------------------------------------
# 4. Masks: a True/False answer for every element
# ---------------------------------------------------------------
# Comparing an array to a number gives an array of True/False values.
is_hot = temps >= HOT_TEMP
print("\nMask for hours 10.8 to 11.2:", is_hot[48:53])

# Use a mask inside [ ] to keep only the elements where it is True.
# hours[is_hot] is "every hour where the temperature is 100 or more."
hot_hours = hours[is_hot]

# [0] takes the first one: the first time the day reaches 100 degrees.
first_hot_time = hot_hours[0]

# ---------------------------------------------------------------
# 5. Count True values with np.sum()
# ---------------------------------------------------------------
# Python treats True as 1 and False as 0, so np.sum() counts the Trues.
# Count the points ABOVE 100, then multiply by the time between points.
hot_count = np.sum(temps > HOT_TEMP)
hours_above_hot = hot_count * TIME_STEP

# ---------------------------------------------------------------
# 6. Print a formatted report
# ---------------------------------------------------------------
# {:<22} = left-align in 22 characters    {:>8} = right-align in 8 characters
# .1f = 1 decimal place                   .2f = 2 decimal places
print()
print("=" * 40)
print(f"{'DAILY HEAT REPORT':^40}")   # ^40 = centered in 40 characters
print("=" * 40)
print(f"{'High temperature:':<22}{peak_temp:>8.1f} F")
print(f"{'Time of high:':<22}{peak_time:>8.2f} h")
print(f"{'Temperature at noon:':<22}{noon_temp:>8.1f} F")
print(f"{'First reaches 100:':<22}{first_hot_time:>8.2f} h")
print(f"{'Hours above 100:':<22}{hours_above_hot:>8.2f} h")
print("=" * 40)

# Why 7.90 hours and not 8? The model is above 100 from 11:00 to 19:00,
# but we only check every 0.1 hours, and the points AT 11.0 and 19.0 equal
# exactly 100 (not above it). The answer is only as precise as the time step.
