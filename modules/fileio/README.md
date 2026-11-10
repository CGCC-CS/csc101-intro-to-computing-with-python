# File I/O & Exceptions

## Objectives

- Opening files for reading and writing
- Reading a whole file and reading a file line by line
- Writing text to a file
- Using the `with` statement so files are closed automatically
- Reading CSV files, both by hand with `split()` and with the `csv` module

## Example code

**Run these examples from inside this folder.** The programs open `data.txt` and `books.csv` by name, so Python looks for those files in the current working directory.

### [readfile.py](./readfile.py)

Opens `data.txt` with a `with` statement, reads the whole file with `read()`, and prints it. This version has no error handling.

### [writefile.py](./writefile.py)

Opens `output.txt` in write mode (`'w'`), writes two lines, and closes the file. Write mode replaces anything already in the file.

### [readingcsv.py](./readingcsv.py)

Reads `books.csv` by hand: gets each line with `readlines()`, removes the newline with `strip()`, and splits each line on commas to build a 2-D list

### [csvmodule.py](./csvmodule.py)

Reads `books.csv` with Python's built-in `csv` module, which correctly handles quoted fields and commas inside fields

## Data files

- [data.txt](./data.txt) - a list of historic computers and the year each was released
- [books.csv](./books.csv) - a list of books with title, author, year, and genre columns

## Related examples

- [Spring 2026 Module 11 - File I/O](../../classexamples/spring2026/csc101_s26_module_11_file_i_o.py)
- [loops2/exceptions.py](../loops2/exceptions.py) and [functions2/errorhandling.py](../functions2/errorhandling.py) - handling exceptions with `try`/`except`
