import os


def calculate_total(price, quantity):
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

        return total


shopping_cart = [
    {
        "name": "apple",
        "price": 0.5,
        "quantity": 4,
    },
    {
        "name": "banana",
        "price": 0.3,
        "quantity": 6,
    },
]
print(calculate_total(shopping_cart))
