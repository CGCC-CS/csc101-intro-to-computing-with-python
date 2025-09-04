"""
This module demonstrates complex expressions and assignment operators in Python.

Author: Wade Huber
Date: August 23, 2025
"""
# Complex expressions and different assignment operators
base_salary = 50000
bonus_rate = 0.12
years_experience = 3

# Complex expression
# Calculate total compensation: 
#        base salary + (base salary × bonus rate × years of experience)
total_compensation = base_salary + (base_salary * bonus_rate * years_experience)
print(f"Total compensation: ${total_compensation:,.2f}")

# Use compound assignment operators to modify variables
base_salary += 5000    # Equivalent to base_salary = base_salary + 5000
print(f"Updated base salary: ${base_salary:,}")

bonus_rate *= 1.1      # Increase bonus rate by 10%

base_salary -= 2000    # Decrease salary by 2000
print(f"Reduced base salary: ${base_salary:,}")

years_experience //= 2 # Integer divide years by 2
print(f"Adjusted years of experience: {years_experience}")
