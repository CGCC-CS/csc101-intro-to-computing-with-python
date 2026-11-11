# Strings

## Objectives

- Creating strings with single, double, and triple quotes
- Escape characters
- String length, indexing, and iterating through characters
- Searching strings with `find()`
- Common string methods: changing case, stripping whitespace, testing contents, and replacing text
- Splitting strings into lists and joining lists into strings

## Example code

### [stringbasics.py](./stringbasics.py)

String creation and quoting (including escaped quotes and multi-line strings), `len()`, indexing with positive and negative indexes, and searching with `find()` (which returns `-1` when the text isn't found)

### [strings.py](./strings.py)

Building a string from a list of characters with `join()`, looping through a string one character at a time, getting a character's ASCII value with `ord()`, concatenating strings with `+`, and `upper()` / `lower()`

### [stringmethods.py](./stringmethods.py)

Common string methods:

- Case conversion: `upper()`, `lower()`, `title()`, `capitalize()`
- Whitespace: `strip()`, `lstrip()`, `rstrip()`
- Testing: `isalpha()`, `isnumeric()`, `isalnum()`
- Replacing text: `replace()`

### [stringsplitting.py](./stringsplitting.py)

Splitting strings with `split()` using different delimiters, the default whitespace split, and a limit on the number of splits. Joining a list back into a string with `join()` using different separators.

## Related class examples

- [Spring 2026 Module 4 - Compound Data Types](../../classexamples/spring2026/csc101_s26_module_4_compound_data_types.py)
- [Fall 2025 Week 4 - Advanced Data Structures](../../classexamples/fall2025/csc101_week_4_in_class_examples.py)
