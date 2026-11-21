"""
budget_tracker.py
CSC101 Module 10 Project: Personal Budget Tracker

Name:
Date:
Description:
"""
import datetime
import math

# Constants -- do not change
TODAY = datetime.date(2027, 4, 1)   # fixed "today" so everyone's output matches
LARGE_EXPENSE = 100                 # expenses over this amount are "large"

# Global scope variables
monthly_budget = 0.0   # total budget for the current month
expenses = []          # list of expense dictionaries
income = []            # list of income dictionaries

# Lambdas (Step 6)
by_amount = None   # TODO: replace None with a lambda that returns an entry's "amount"
is_large = None    # TODO: replace None with a lambda: True if an entry's amount > LARGE_EXPENSE


def to_date(date):
    """Return a datetime.date. None means TODAY; a string must be "YYYY-MM-DD".

    This function is complete. A badly formatted string raises ValueError.
    """
    if date is None:
        return TODAY
    if type(date) == str:
        return datetime.date.fromisoformat(date)
    return date


def set_monthly_budget(amount, currency="USD"):
    """Set the monthly budget.

    Raises ValueError("Budget cannot be negative.") if amount < 0.
    Returns: "Monthly budget set to 2,500.00 USD."
    """
    pass


def add_expense(amount, category="miscellaneous", description="", date=None):
    """Add an expense dictionary to expenses.

    Raises ValueError("Expense amount must be greater than 0.") if amount <= 0.
    Keys: "amount" (float), "category" (lowercase), "description", "date" (use to_date)
    Returns: "Added expense: $75.50 in 'food' on 2027-03-30."
    """
    pass


def add_income(amount, source="salary", date=None):
    """Add an income dictionary to income.

    Raises ValueError("Income amount must be greater than 0.") if amount <= 0.
    Keys: "amount" (float), "source" (lowercase), "date" (use to_date)
    Returns: "Added income: $3,200.00 from 'salary' on 2027-04-01."
    """
    pass


def get_remaining_budget():
    """Return monthly_budget minus the total of all expenses, rounded to 2 decimals."""
    pass


def get_totals():
    """Return a tuple (total_income, total_spent, balance), each rounded to 2 decimals.

    balance = total_income - total_spent
    """
    pass


def daily_allowance(days_left=30):
    """Return the remaining budget per day, rounded DOWN to whole dollars (math.floor)."""
    pass


def analyze_spending(category=None, min_amount=0, max_amount=None):
    """Return a dict {"count": int, "total": float, "average": float} for matching expenses.

    An expense matches when ALL of these hold:
        category is None, or the expense's category equals category.lower()
        the amount is >= min_amount
        max_amount is None, or the amount is <= max_amount
    total and average are rounded to 2 decimals; average is 0.0 when count is 0.
    """
    pass


def get_spending_report(*categories):
    """Return a dict {category: total spent} for each category name given.

    Names are lowercased. Include a category even when its total is 0.0.
    Hint: call analyze_spending() for each name.
    """
    pass


def top_expenses(n=3):
    """Return a list of the n largest expenses, largest first.

    Use sorted() with key=by_amount, then slice.
    """
    pass


def large_expenses():
    """Return a list of the expenses over LARGE_EXPENSE. Use filter() with is_large."""
    pass


# Step 7: add the if __name__ == "__main__": demo block here
