# CSC101: Introduction to Computing with Python - Class Examples (Spring 2026)

This directory contains Python files downloaded from Google Colab notebooks used as in-class examples. Each file demonstrates fundamental and advanced Python programming concepts.

Generated with Claude Cowork May 6, 2026

## Table of Contents

- [Core Python Basics](#core-python-basics)
- [Data Structures](#data-structures)
- [Control Flow](#control-flow)
- [Functions & Modules](#functions--modules)
- [Object-Oriented Programming](#object-oriented-programming)
- [File I/O](#file-io)
- [AI & Machine Learning](#ai--machine-learning)

---

## Core Python Basics

### [csc101_review.py](csc101_review.py) **Comprehensive Python Review**

A thorough review covering all fundamental Python concepts including:

- Print statements and data types (strings, integers, floats, booleans)
- User input with `input()`
- Arithmetic operators and string manipulation
- Boolean operations and comparisons
- Conditional statements (if/elif/else) with AND/OR/NOT logic
- While and for loops with ranges and steps
- Lists, dictionaries with basic operations
- Function definitions with parameters and return values
- Function scope (global vs local variables)
- The `random` module for generating random numbers
- Simple class definitions with attributes and methods
- Parameter vs argument terminology

### [csc101_s26_module_3_variables_&_expressions.py](csc101_s26_module_3_variables_&_expressions.py) **Variables, Data Types & Expressions**

Focuses on variable declaration and expression evaluation:

- Comments (single-line and multi-line)
- Variable assignment and dynamic typing in Python
- All arithmetic operators (+, -, *, /, //, %, **)
- Operator precedence and associativity
- F-string formatting with various options
- Evaluation of complex expressions with parentheses
- User input and type conversion with `int()`
- Output formatting techniques
- Constants by convention (ALL_CAPS naming)

---

## Data Structures

### [csc101_s26_module_4_compound_data_types.py](csc101_s26_module_4_compound_data_types.py) **Strings, Lists, Tuples, Sets & Dictionaries**

Comprehensive coverage of Python's compound data types:

- String operations: upper(), lower(), capitalize(), strip(), split(), replace(), find()
- Multiline strings and escape characters (\n, \t)
- List creation, indexing, slicing, and methods (append, insert, remove, sort, pop)
- Tuple creation and unpacking
- Set operations: add(), union(), intersection(), difference(), symmetric_difference()
- Removing duplicates from lists using sets
- Dictionary creation, access, modification, and iteration
- Dictionary methods: keys(), values(), items()
- Indexing and slicing for strings and lists

---

## Control Flow

### [csc101_s26_module_5_conditionals.py](csc101_s26_module_5_conditionals.py) **Conditional Statements**

Mastering decision-making in Python:

- String operations review (strip, split, upper, lower, join)
- If/else statements
- If/elif/else chains for multiple conditions
- Comparison operators (==, !=, >, >=, <, <=)
- Logical operators (and, or, not)
- Boolean evaluation in conditional statements
- Real-world examples with user input and grade assignments

### [csc101_s26_module_6_loops.py](csc101_s26_module_6_loops.py) **Loop Structures**

Understanding iteration with while and for loops:

- While loops with various counter patterns (incrementing, decrementing, by steps)
- Accumulation pattern (summing numbers)
- Sentinel values to control loop termination
- For loops with range() function
- Range variations: range(n), range(start, end), range(start, end, step)
- Iterating through strings, lists, and dictionaries
- Dictionary iteration with .items() method
- Enumerate function for index-based iteration
- Loop control and output formatting

### [csc101_s26_module_7_nested_loops_&_exceptions.py](csc101_s26_module_7_nested_loops_&_exceptions.py) **Nested Loops & Exception Handling**

Advanced loop structures and error management:

- Nested loops for multiplication tables, rectangles, and triangles
- Nested conditionals within loops
- String building with loops
- List iteration with nested loops
- Character substitution using dictionaries in loops
- Try/except blocks for exception handling
- ValueError handling (invalid input conversion)
- ZeroDivisionError handling
- Multiple except clauses
- Retry loops with exception handling

---

## Functions & Modules

### [csc101_s26_module_8_functions.py](csc101_s26_module_8_functions.py) **Function Definitions & Usage**

Creating and using functions effectively:

- Function definitions with and without parameters
- Return statements and return values
- Function calls and argument passing
- Docstrings for documentation
- Functions with multiple parameters
- Returning multiple values as tuples
- Using functions in loops
- Practical examples: square calculation, voter age checking, min/max finding
- Visual output functions (diamond and table printing)
- Integration with the math module

### [csc101_s26_module_9_advanced_functions,_modules,_&_lambdas.py](csc101_s26_module_9_advanced_functions,_modules,_&_lambdas.py) **Advanced Functions, Modules & Lambda Expressions**

Working with Python's module system and advanced function features:

- Module imports (basic, multiple, selective, aliased)
- Using the math module: sqrt(), sin(), cos(), tan(), pi
- Using the datetime module for current time and timezone handling
- Default parameter values in functions
- Keyword arguments in function calls
- Variable-length arguments (*args)
- Keyword arguments (**kwargs)
- Lambda expressions (anonymous functions)
- Using lambdas for simple operations (squaring, even/odd checking)

---

## Object-Oriented Programming

### [csc101_s26_module_10_classes.py](csc101_s26_module_10_classes.py) **Classes & Object-Oriented Programming**

Introduction to OOP with class definitions:

- Class definitions and the `__init__` constructor
- Instance attributes and class attributes
- Instance methods
- Creating and using class instances
- The Die class with state and behavior
- Rolling a die with random number generation
- The `__str__` method for string representation
- Practical example: simulating dice rolls
- Understanding the difference between class and instance attributes

---

## File I/O

### [csc101_s26_module_11_file_i_o.py](csc101_s26_module_11_file_i_o.py) **File Input/Output Operations**

Reading from and writing to files:

- Opening files in write mode ('w')
- Writing text to files with .write()
- Opening files in read mode ('r')
- Reading entire file contents with .read()
- Using context managers (with statement)
- Reading files line by line
- Line counting and strip() method
- Reading files in chunks (bulk read operations)
- Proper file closing and resource management
- Working with text files containing lists of names

---

## AI & Machine Learning

### [csc101_s26_module_12_ai_with_python.py](csc101_s26_module_12_ai_with_python.py) **Machine Learning with PyTorch**

Building and training a neural network for classification:

- Importing ML libraries: matplotlib, pandas, PyTorch, scikit-learn
- Loading the Iris dataset from a remote CSV
- Data exploration with head() and tail() methods
- Converting categorical data to numeric codes
- Train/test split with scikit-learn
- Converting data to PyTorch tensors
- Building a neural network class (IrisModel) with:
  - Input layer (4 features)
  - Two hidden layers (8 and 12 nodes)
  - Output layer (3 classes)
- Activation functions (ReLU)
- Loss function (CrossEntropyLoss)
- Optimizer (Adam)
- Training loop over multiple epochs
- Evaluating model performance
- Making predictions on new data
- Saving and loading trained models
- Softmax and argmax for class prediction

---

## How to Use These Files

1. **Download to Your Local Machine**: Clone or download this repository
2. **Run in Google Colab**: Each file includes a link to the original Colab notebook at the top
3. **Run Locally**: Use Python 3.x with appropriate libraries installed:

   ```bash
   # For basic examples
   python csc101_review.py
   
   # For ML example (requires additional libraries)
   # pip install torch pandas scikit-learn matplotlib
   python csc101_s26_module_12_ai_with_python.py
   ```

## Prerequisites

- Python 3.6+
- For most modules: no additional packages needed
- For Module 12 (AI): PyTorch, pandas, scikit-learn, matplotlib

## Learning Outcomes

By working through these examples, students will understand:

- Python syntax and basic programming concepts
- Data structure manipulation and operations
- Control flow and program logic
- Function design and modular programming
- Object-oriented programming principles
- File handling and data persistence
- Introduction to machine learning and neural networks

## Instructor

Wade Huber (wade.huber@cgc.edu)

## Note

These files are automatically generated from Google Colab notebooks. For the interactive experience and to run the code directly, visit the original Colab links at the top of each file.
