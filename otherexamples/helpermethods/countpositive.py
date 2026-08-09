"""Count the positive numbers in a list.

This module demonstrates a simple helper function (is_positive)
that isolates the decision "is this number positive?" so the main
function can focus on iterating through the list.
"""

def is_positive(n):
    """Return True if n is greater than zero, otherwise False."""
    return n > 0

def count_positive(nums):
    """Return the number of positive values in the list nums."""
    count = 0
    for n in nums:
        if is_positive(n):
            count += 1
    return count

# -------------------------------------------------
# Simple test helper
# -------------------------------------------------

def check_expect(actual, expected):
    """Print PASS if actual equals expected, otherwise print a failure message."""
    if actual == expected:
        print("PASS")
    else:
        print(f"FAIL: got {actual}, expected {expected}")

# -------------------------------------------------
# Tests for is_positive
# -------------------------------------------------

check_expect(is_positive(5), True)
check_expect(is_positive(1), True)
check_expect(is_positive(0), False)
check_expect(is_positive(-3), False)
check_expect(is_positive(0.5), True)
check_expect(is_positive(-0.1), False)

# -------------------------------------------------
# Tests for count_positive
# -------------------------------------------------

check_expect(count_positive([]), 0)
check_expect(count_positive([1, 2, 3]), 3)
check_expect(count_positive([-1, -2, -3]), 0)
check_expect(count_positive([1, -2, 3, -4, 5]), 3)
check_expect(count_positive([0, 0, 0]), 0)
check_expect(count_positive([-5, 0, 7]), 1)
check_expect(count_positive([10]), 1)
check_expect(count_positive([-10]), 0)
check_expect(count_positive([1, 0, -1, 2, 0, 3]), 3)
