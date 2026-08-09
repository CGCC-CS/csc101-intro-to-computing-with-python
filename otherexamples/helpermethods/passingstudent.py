"""Filter a list of students to those who passed.

The helper passed() encapsulates the multi-part rule for what
counts as passing (score, assignments, academic hold). The main
function passing_students then simply keeps the students for
whom that rule returns True.
"""

# -------------------------------------------------
# Helper function
# -------------------------------------------------

def passed(student):
    """Return True if the student meets all passing criteria.
 
    A student passes when:
      - score >= 70
      - assignments completed >= 8
      - no academic hold
    """
    return (student["score"] >= 70 and
            student["assignments"] >= 8 and
            not student["academic_hold"])

# -------------------------------------------------
# Primary function
# -------------------------------------------------
def passing_students(students):
    """Return a new list containing only the students who passed."""
    return [s for s in students if passed(s)]

# -------------------------------------------------
# Example data
# -------------------------------------------------

test_students = [
    {"name": "Alice", "score": 85, "assignments": 10, "academic_hold": False}, # passes
    {"name": "Bob",   "score": 65, "assignments":  9, "academic_hold": False}, # fails (score)
    {"name": "Carol", "score": 90, "assignments":  7, "academic_hold": False}, # fails (assignments)
    {"name": "Dave",  "score": 78, "assignments": 12, "academic_hold": True},  # fails (hold)
    {"name": "Eve",   "score": 72, "assignments":  8, "academic_hold": False}, # passes (borderline)
]

# -------------------------------------------------
# Quick demonstration
# -------------------------------------------------

if __name__ == "__main__":
    result = passing_students(test_students)

    print("Students who passed:")
    for s in result:
        print(f"  - {s['name']}")

    # Simple assertions (act as tests)
    assert passed(test_students[0]) is True
    assert passed(test_students[1]) is False
    assert passed(test_students[2]) is False
    assert passed(test_students[3]) is False
    assert passed(test_students[4]) is True

    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[1]["name"] == "Eve"

    print("\nAll tests passed.")
