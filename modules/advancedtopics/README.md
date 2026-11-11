# Advanced Topics: Comprehensions & Recursion

## Objectives

- Creating lists, sets, and dictionaries with comprehensions
- Filtering with an `if` inside a comprehension
- Writing recursive functions with a base case and a recursive case
- Comparing recursive solutions

## Example code

### [comprehensionsintro.py](./comprehensionsintro.py)

Compares building lists with a loop to building them with a list comprehension, then introduces set comprehensions, dictionary comprehensions (including one built with `zip()`), a comprehension with two `for` clauses, and shortcuts like `list()` and `dict(zip(...))`

### [recursion.py](./recursion.py)

Recursive functions:

- `fib()` - a simple recursive Fibonacci function
- `fib_tail()` - a tail-recursive Fibonacci function that uses a helper function and is much faster for large values
- `find_in_array()` - searching a list recursively by checking the first item and then searching the rest of the list
