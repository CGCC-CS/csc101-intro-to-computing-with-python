# CSC101 Debugging 2 — The Shipping Calculator
# Fix the existing program; do not rewrite it from scratch.

order_total = 75
if order_total >= 50:
    shipping = 5
elif order_total >= 100:
    shipping = 0
else:
    shipping = 10
print("Shipping:", shipping)
