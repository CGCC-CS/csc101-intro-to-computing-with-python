# Lists, Tuples, Sets, & Dictionaries

## Objectives

- Creating and using lists, tuples, sets, and dictionaries
- Indexing and slicing lists and tuples
- Using list, set, and dictionary methods
- Tuple unpacking and immutability
- Set operations: union, intersection, and difference
- Accessing, adding, and updating dictionary key-value pairs
- Choosing the right data structure for a problem

## Example code

### Lists

#### [arrays.py](./arrays.py)

A short introduction to Python lists (what other languages call arrays): creating lists, building a list with `append()` in a loop, `len()`, and adding up the values in a list with a loop

#### [listbasics.py](./listbasics.py)

Creating lists, indexing (including negative indexes), slicing, `len()`, and using list elements in math expressions. Points out that the last index is `len() - 1`.

#### [listmethods.py](./listmethods.py)

List methods: `append()`, `insert()`, `extend()`, `remove()`, `pop()`, `count()`, `index()`, `sort()`, and `reverse()`

### Tuples

#### [tuples.py](./tuples.py)

Creating tuples (including a single-item tuple), indexing, unpacking, the `count()` and `index()` methods, and what happens when you try to change a tuple

### Sets

#### [sets.py](./sets.py)

Creating sets, how sets remove duplicates, checking membership with `in`, `add()`, `remove()`, `discard()`, `pop()`, and the union (`|`), intersection (`&`), and difference (`-`) operators

### Dictionaries

#### [dictionaries.py](./dictionaries.py)

Creating dictionaries, accessing and changing values, adding new key-value pairs, `keys()`, `values()`, `items()`, safe access with `get()`, and checking for a key with `in`

### Putting it all together

#### [emptycollections.py](./emptycollections.py)

Creating empty strings, lists, tuples, sets, and dictionaries. Shows that empty collections have a length of 0 and are `False` in a boolean test. Note: `{}` creates an empty *dictionary* - use `set()` for an empty set.

#### [comparingstructures.py](./comparingstructures.py)

The same data stored in a list, tuple, set, and dictionary, with a table comparing which ones are ordered, mutable, allow duplicates, and support indexing

#### [liststuplesdictionaries.py](./liststuplesdictionaries.py)

A longer reference covering lists, tuples, and dictionaries, including list and dictionary comprehensions, named tuples, nested dictionaries, and converting between types. Ends with practical examples: a shopping cart, student grade averages, a word frequency counter, and the distance along a path of coordinates.

#### [grademanagementsystem.py](./grademanagementsystem.py)

A larger example program that manages student grades. Uses a dictionary of students, a set of subjects, a list of grade history, and a tuple of grade boundaries, and organizes the work into functions. Includes bonus examples of string formatting, cleaning input, and `split()` / `join()`.

## Related class examples

- [Spring 2026 Module 4 - Compound Data Types](../../classexamples/spring2026/csc101_s26_module_4_compound_data_types.py)
- [Fall 2025 Week 4 - Advanced Data Structures](../../classexamples/fall2025/csc101_week_4_in_class_examples.py)
