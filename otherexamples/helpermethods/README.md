# Helper Methods — Python Examples

These four Python programs accompany the **Helper Methods** notes used in the
CS1 courses (and referenced in CSC240). Each one shows the same core idea: take
a larger task, find the smaller well-defined question hiding inside it, and give
that question its own small function — a *helper*. The main function is then left
to focus on the larger job of walking through a collection or orchestrating steps.

All examples are plain Python 3 with no third-party dependencies.

## Running the examples

Each file runs on its own from a terminal:

```(bash)
python countpositive.py
python validusername.py
python passingstudent.py
python customerorder.py
```

`countpositive.py` and `validusername.py` print a line of `PASS` results as they
run their built-in checks. `passingstudent.py` and `customerorder.py` print a
short demonstration of their output. No input is required.

## The files

### countpositive.py — counting the positive numbers in a list

The helper `is_positive(n)` answers one question: *is this number positive?*
The main function `count_positive(nums)` then focuses purely on walking through
the list and counting. A small `check_expect` helper prints `PASS`/`FAIL` for a
set of test cases covering empty lists, all-positive, all-negative, zeros, and
floats.

- Helper: `is_positive(n)`
- Main: `count_positive(nums)`

### validusername.py — checking whether a string is a valid username

Validation rules tend to grow into a tangle of conditions. Here they are
isolated in `is_valid_username(name)`, which is `True` when the name is 3–16
characters, contains only alphanumeric characters, and does not start with a
digit. The main function `filter_valid_usernames(names)` becomes a clean
one-line list comprehension. The length check is written first so that the
later `name[0]` lookup is always safe. `check_expect` drives a set of tests
covering length limits, leading digits, spaces, and punctuation.

- Helper: `is_valid_username(name)`
- Main: `filter_valid_usernames(names)`

### passingstudent.py — filtering the students who passed

The rule for what counts as "passing" is non-trivial: a score of at least 70,
at least 8 assignments completed, and no academic hold. Bundling that rule into
`passed(student)` keeps the filtering logic readable and makes the rule easy to
change or test in one place. `passing_students(students)` is then a simple list
comprehension. The file includes sample student records and `assert`-based
tests that run when the file is executed directly.

- Helper: `passed(student)`
- Main: `passing_students(students)`

### customerorder.py — calculating a customer's final total

The overall job splits naturally into three smaller tasks, each with its own
helper: `subtotal(items)` sums price × quantity, `apply_discount(amount, coupon)`
applies a coupon when one is valid, and `add_tax(amount, state)` (using
`tax_rate_for(state)`) looks up and applies sales tax. The main function
`final_total(order)` just orchestrates the three steps in order. Note that the
coupon's `percent_off` is treated as a whole-number percent and divided by 100,
and a missing coupon (`None`) is handled gracefully. Running the file prints the
totals for two sample orders.

- Helpers: `subtotal(items)`, `apply_discount(amount, coupon)`, `tax_rate_for(state)`, `add_tax(amount, state)`
- Main: `final_total(order)`

## The pattern to notice

In every example the shape is the same: a small helper owns one focused question
or step, and a larger function owns the job of processing a collection or
sequencing the work. When you find yourself thinking *"first I need to figure out
___,"* that blank is usually a good candidate for a helper.
