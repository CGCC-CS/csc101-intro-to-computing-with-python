class BankAccount:
    # Class attribute (shared by all instances)
    interest_rate = 0.02
    
    def __init__(self, owner, balance=0):
        # Instance attributes (unique to each object)
        self.owner = owner
        self.balance = balance

# Create two instances
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

print(acc1.interest_rate)  # → 0.02
print(acc2.interest_rate)  # → 0.02
print(BankAccount.interest_rate)  # → 0.02

# Change class attribute → affects ALL instances
BankAccount.interest_rate = 0.03

print(acc1.interest_rate)  # → 0.03
print(acc2.interest_rate)  # → 0.03

# Instance attributes are independent
acc1.balance = 2000
print(acc1.balance)  # → 2000
print(acc2.balance)  # → 500 (unchanged)