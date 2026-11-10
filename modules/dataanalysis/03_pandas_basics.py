# Module 13 Example 3: Pandas Basics
# CSC101 - Introduction to Computing with Python
# Loads a small CSV file into a DataFrame, explores it, and cleans up
# missing data.

import pandas as pd  # "pd" is the standard nickname (alias) for Pandas

# ---------------------------------------------------------------
# 0. Make a small CSV file to work with
# ---------------------------------------------------------------
# Usually the CSV file already exists. Here we write one first so this
# example runs anywhere (VS Code or Colab) with no download.
# Two of the values are blank on purpose: that is "missing data".
csv_text = """city,month,high_temp,rain_inches
Chandler,Jan,67,0.9
Chandler,Apr,85,0.3
Chandler,Jul,106,
Chandler,Oct,88,0.6
Flagstaff,Jan,43,2.0
Flagstaff,Apr,57,1.2
Flagstaff,Jul,,2.8
Flagstaff,Oct,63,1.8
"""
with open("weather.csv", "w") as file:
    file.write(csv_text)

# ---------------------------------------------------------------
# 1. Load the CSV file into a DataFrame
# ---------------------------------------------------------------
# A DataFrame is a table: rows and named columns, like a spreadsheet.
weather = pd.read_csv("weather.csv")

print("The whole table:")
print(weather)

# ---------------------------------------------------------------
# 2. Look at the data
# ---------------------------------------------------------------
print("\nFirst 3 rows (.head(3)):")
print(weather.head(3))

print("\nLast 2 rows (.tail(2)):")
print(weather.tail(2))

print("\nRows and columns (.shape):", weather.shape)

# .describe() gives count, mean, min, max, and more for number columns.
print("\nBasic statistics (.describe()):")
print(weather.describe())

# ---------------------------------------------------------------
# 3. Select columns and filter rows
# ---------------------------------------------------------------
# One column: use its name in [ ], like a dictionary key.
print("\nJust the high_temp column:")
print(weather["high_temp"])

# Several columns: put a LIST of names inside the [ ].
print("\nCity and month only:")
print(weather[["city", "month"]])

# Filter rows with a condition (this works like a NumPy mask).
print("\nRows where high_temp is over 80:")
print(weather[weather["high_temp"] > 80])

print("\nOnly Flagstaff:")
print(weather[weather["city"] == "Flagstaff"])

# ---------------------------------------------------------------
# 4. Find and handle missing data
# ---------------------------------------------------------------
# Blank cells become NaN ("Not a Number").
# .isnull().sum() counts the missing values in each column.
print("\nMissing values per column:")
print(weather.isnull().sum())

# Strategy 1: remove every row that has a missing value.
dropped = weather.dropna()
print("\nAfter .dropna() (rows with blanks removed):")
print(dropped)

# Strategy 2: fill the blanks with a value instead.
# Here, missing rain becomes 0 and a missing temperature becomes the
# column's average (rounded to 1 decimal). Filling is a guess: the average
# of BOTH cities is a poor guess for Flagstaff in July, so always think
# about whether the fill value makes sense.
filled = weather.copy()
filled["rain_inches"] = filled["rain_inches"].fillna(0)
average_high = round(filled["high_temp"].mean(), 1)
filled["high_temp"] = filled["high_temp"].fillna(average_high)
print("\nAfter .fillna() (blanks filled in):")
print(filled)

# ---------------------------------------------------------------
# 5. Statistics on one column
# ---------------------------------------------------------------
print(f"\nAverage high temp: {weather['high_temp'].mean():.1f} F")
print(f"Highest high temp: {weather['high_temp'].max():.0f} F")
print(f"Total rain:        {weather['rain_inches'].sum():.1f} in")
