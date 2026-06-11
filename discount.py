# discount.py

def calculate_discount(current_total, order_amount):
    total_after_order = current_total + order_amount

    if total_after_order >= 50000000:
        return 0.1

    return 0


def calculate_payment(current_total, order_amount):
    discount_rate = calculate_discount(current_total, order_amount)

    return order_amount * (1 - discount_rate)