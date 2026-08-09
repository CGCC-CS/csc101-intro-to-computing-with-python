"""
Filter a list of students to those who passed.

The helper passed() encapsulates the multi-part rule for what
counts as passing (score, assignments, academic hold). The main
function passing_students then simply keeps the students for
whom that rule returns True.
"""
# -------------------------------------------------
# Functions
# -------------------------------------------------

def is_valid_username(name):
    """Return True if name is a valid username.
    
    A valid username:
      - is between 3 and 16 characters long (inclusive)
      - contains only alphanumeric characters
      - does not start with a digit
    """
    return (3 <= len(name) <= 16 and
            name.isalnum() and
            not name[0].isdigit())

def filter_valid_usernames(names):
    """Return a new list containing only the valid usernames from names."""
    return [name for name in names if is_valid_username(name)]

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
# Tests for is_valid_username
# -------------------------------------------------

check_expect(is_valid_username("alice"), True)
check_expect(is_valid_username("Bob42"), True)
check_expect(is_valid_username("a1b2c3"), True)
check_expect(is_valid_username("ab"), False)                  # too short
check_expect(is_valid_username("abcdefghijklmnopq"), False)   # too long (17 chars)
check_expect(is_valid_username("1alice"), False)              # starts with digit
check_expect(is_valid_username("alice!"), False)              # non-alphanumeric
check_expect(is_valid_username("alice bob"), False)           # space
check_expect(is_valid_username("Alice"), True)
check_expect(is_valid_username("a"), False)                   # too short
check_expect(is_valid_username("abcdefghijklmnop"), True)     # exactly 16 chars

# -------------------------------------------------
# Tests for filter_valid_usernames
# -------------------------------------------------

check_expect(filter_valid_usernames([]), [])

check_expect(filter_valid_usernames(["alice", "bob", "carol"]),
             ["alice", "bob", "carol"])

check_expect(filter_valid_usernames(["ab", "alice", "2bob", "carol!"]),
             ["alice"])

check_expect(filter_valid_usernames(["1start", "too_long_username_here", "okname", "x"]),
             ["okname"])

check_expect(filter_valid_usernames(["a", "ab", "abc", "abcd"]),
             ["abc", "abcd"])
