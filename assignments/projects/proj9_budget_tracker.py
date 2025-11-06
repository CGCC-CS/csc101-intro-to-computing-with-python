# Required imports
import datetime
import math

# Global scope variables
monthly_budget = 0.0   # Total budget for the current month
expenses = []          # List of expense dictionaries
income = []            # List of income dictionaries


def set_monthly_budget(amount, currency="USD"):
    """
    Set the monthly budget with validation.

    Args:
        amount (float or int): Must be >= 0
        currency (str): Default "USD"

    Raises:
        TypeError: If amount is not a number
        ValueError: If amount is negative

    Returns:
        str: Confirmation message with formatted amount and currency
    """
    pass

def add_expense(amount, category="miscellaneous", description="", date=None):
    """
    Add an expense entry.

    Args:
        amount (float or int): Must be > 0
        category (str): Converted to lowercase
        description (str): Optional
        date (datetime.date or str): If None → today. If str → must be "YYYY-MM-DD"

    Raises:
        Appropriate errors for invalid types/formats

    Returns:
        str: Confirmation message
    """
    pass

def add_income(amount, source="salary", date=None):
    """
    Add an income entry.

    Same rules as add_expense for amount and date.
    """
    pass

def get_remaining_budget():
    """
    Returns:
        float: monthly_budget minus sum of all expense amounts, rounded to 2 decimals
    """
    pass

