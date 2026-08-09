"""Calculate the final total for a customer order.

The work is split into clear helpers:
  - subtotal: sum of item prices × quantities
  - apply_discount: apply a coupon if it is valid
  - tax_rate_for / add_tax: look up and apply sales tax

The main function final_total simply orchestrates these steps.
"""

# -------------------------------------------------
# Helper functions
# -------------------------------------------------

def subtotal(items):
    """Return the subtotal for a list of items.

    Each item is a dict with 'price' and 'quantity' keys.
    """
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

def apply_discount(amount, coupon):
    """Apply a percentage discount if the coupon is valid.

    coupon is either None or a dict with 'valid' and 'percent_off' keys.
    Returns the discounted amount (or the original amount if no valid coupon).
    """
    ret = amount

    if coupon is not None and coupon.get("valid", False):
        ret = amount * (1 - coupon["percent_off"] / 100.0)

    return ret

def tax_rate_for(state):
    """Return the sales-tax rate for the given state code.

    Uses a small built-in table; defaults to 5% for unknown states.
    """
    rates = {
        "CA": 0.075,
        "NY": 0.08,
        "TX": 0.0625,
        "FL": 0.06
    }
    return rates.get(state, 0.05)   # default 5%

def add_tax(amount, state):
    """Return the amount after adding the sales tax for the given state."""
    rate = tax_rate_for(state)
    return amount * (1 + rate)

# -------------------------------------------------
# Main function
# -------------------------------------------------

def final_total(order):
    """Compute the final total for an order.

    order is a dict containing:
      - 'items': list of item dicts
      - 'coupon': optional coupon dict or None
      - 'state': two-letter state code
    """
    sub = subtotal(order["items"])
    after_discount = apply_discount(sub, order.get("coupon"))
    return add_tax(after_discount, order["state"])

# -------------------------------------------------
# Example usage
# -------------------------------------------------

if __name__ == "__main__":
    order1 = {
        "items": [
            {"price": 20.00, "quantity": 2},
            {"price": 15.50, "quantity": 1}
        ],
        "coupon": {"valid": True, "percent_off": 10},
        "state": "CA"
    }

    order2 = {
        "items": [
            {"price": 50.00, "quantity": 1}
        ],
        "coupon": None,          # no coupon
        "state": "NY"
    }

    print(f"Order 1 total: ${final_total(order1):.2f}")
    print(f"Order 2 total: ${final_total(order2):.2f}")
