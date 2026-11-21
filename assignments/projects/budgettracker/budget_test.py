"""
budget_test.py
CSC101 Module 10 Project: Personal Budget Tracker -- test program

Name:
Date:
Description:
"""
# TODO Step 8a: import budget_tracker as bt
# TODO Step 8a: from budget_tracker import get_totals and top_expenses

# TODO Step 8b: money = a lambda that formats a number as "$1,234.50"

# Test 1 data -- do not change
print("=== Budget Tracker Test: April 1, 2027 ===")
print(bt.set_monthly_budget(2500))
print(bt.add_income(3200))
print(bt.add_income(250, "Tutoring", date="2027-03-28"))
print(bt.add_expense(75.50, "Food", "Lunch", "2027-03-30"))
print(bt.add_expense(150, "food", "Groceries"))
print(bt.add_expense(1200, "Rent", "April rent", "2027-04-01"))
print(bt.add_expense(45.99, "utilities", "Phone"))
print(bt.add_expense(19.99, description="Movie"))
print(bt.add_expense(amount=62.40, category="Transport", description="Gas", date="2027-03-31"))

# TODO Step 8c: Totals
# TODO Step 8d: Spending analysis
# TODO Step 8e: Top 3 expenses and large expenses
# TODO Step 8f: Error handling
