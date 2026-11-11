# Module 13: Python Libraries for Data Science

Code examples for CSC101 Module 13. Each file is a short, heavily commented program you can run, read, and change. Work through them in order.

| # | File | Library | What it shows |
|---|---|---|---|
| 1 | `01_numpy_basics.py` | NumPy | Creating arrays, math on a whole array at once, `.size`, indexing and slicing, `np.min()`, `np.max()`, `np.mean()`, `np.sum()`, `np.arange()`, `np.linspace()` |
| 2 | `02_numpy_modeling.py` | NumPy | Modeling a hot day in Chandler: named constants, a function that works on one number **or** a whole array, `np.argmax()`, masks, `[0]`, counting with `np.sum()`, and a formatted report |
| 3 | `03_pandas_basics.py` | Pandas | Loading a CSV file into a DataFrame, `.head()`, `.tail()`, `.shape`, `.describe()`, selecting columns, filtering rows, and finding and handling missing data |
| 4 | `04_matplotlib_basics.py` | Matplotlib | A line plot with a reference line, a bar plot, a scatter plot, and a histogram, each with a title and axis labels |

## How to run the examples

**Google Colab (no setup):** NumPy, Pandas, and Matplotlib are already installed. Create a new notebook, paste the code into a cell, and run it.

**VS Code:** Install the libraries once. Open the terminal and run:

```
pip install numpy pandas matplotlib
```

If `pip` is not found, try `python -m pip install numpy pandas matplotlib` (Windows) or `python3 -m pip install numpy pandas matplotlib` (Mac).

Then open an example and click **Run**. For `04_matplotlib_basics.py`, the program pauses while the chart windows are open. Close them to end the program.

## Using these examples for the project

`02_numpy_modeling.py` uses the same tools as the **Artemis II Splashdown Model** project, but a different model. It models temperature over a day instead of a capsule's height over time. Use it to see how each tool works, then apply the same steps to the project.

| Project step | Where to look in Example 2 |
|---|---|
| Import with standard aliases | Top of the file (`import numpy as np`) |
| Named constants | The `START_HOUR` ... `HOT_TEMP` block |
| A function with a docstring and no loop | `temperature(hour)` |
| Time array with `np.linspace()` | Section 1 |
| `.size` and slicing with `[:3]` | Section 1 |
| Calling the function with a single number | Section 2 |
| Finding a peak with `np.argmax()` | Section 3 |
| Mask, filter, and `[0]` for the first match | Section 4 |
| `np.sum()` on a mask times the time step | Section 5 |
| Report with `=` borders, centering, `:<22` and `:>8` | Section 6 |

For the graph, see Chart 1 in `04_matplotlib_basics.py`. It plots two lines on the same graph and adds a dashed reference line with `plt.axhline()`, a title, axis labels, a grid, and a legend. It also calls `plt.show()` last.

## Quick reference

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy
values = np.array([3, 1, 4])        # list -> array
values * 2                          # math on every element: [6 2 8]
np.linspace(0, 1, 5)                # 5 evenly spaced values, end included
np.argmax(values)                   # index of the largest value: 2
values > 2                          # mask: [ True False  True]
values[values > 2]                  # keep only the True positions: [3 4]
np.sum(values > 2)                  # count the Trues: 2

# Pandas
data = pd.read_csv("file.csv")      # CSV file -> DataFrame
data.head()                         # first 5 rows
data["column"]                      # one column
data[data["column"] > 10]           # filter rows
data.isnull().sum()                 # missing values per column

# Matplotlib
plt.plot(x, y, label="name")        # line plot
plt.bar(categories, amounts)        # bar plot
plt.scatter(x, y)                   # scatter plot
plt.hist(values, bins=5)            # histogram
plt.title("Title")
plt.xlabel("x label")
plt.ylabel("y label")
plt.legend()
plt.show()                          # always last
```

## Common mistakes

- **`ModuleNotFoundError: No module named 'numpy'`**: The library is not installed in VS Code. Run the `pip install` command above.
- **List vs. array math**: `[1, 2] + [3, 4]` joins two lists into `[1, 2, 3, 4]`. `np.array([1, 2]) + np.array([3, 4])` adds them to get `[4 6]`. Turn a list into an array before doing math.
- **`np.max()` vs. `np.argmax()`**: `np.max()` gives the largest *value*. `np.argmax()` gives its *position* (index), which you can use to look up a matching value in another array.
- **`IndexError` after a mask**: `values[mask][0]` fails if nothing in the mask is True. Check that the condition can actually happen in your data.
- **Chart not showing**: Make sure `plt.show()` is the last line and that the program has finished printing.

## Course alignment

Competencies 4 (functions, modules, and libraries), 6 (implement algorithms), and 7 (using objects from libraries). Outline VII.B.1–VII.B.2.
