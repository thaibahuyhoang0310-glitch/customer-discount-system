# discount.py

def calculate_discount(current_total, order_amount):
    """
    current_total: Tổng giá trị mua hàng trước đơn hàng hiện tại
    order_amount: Giá trị đơn hàng hiện tại

    Trả về:
        0.1 : được giảm giá 10%
        0   : không được giảm giá
    """

    total_after_order = current_total + order_amount

    if total_after_order >= 50000000:
        return 0.1

    return 0


def calculate_payment(current_total, order_amount):
    """
    Tính số tiền phải thanh toán sau giảm giá
    """

    discount_rate = calculate_discount(current_total, order_amount)

    return order_amount * (1 - discount_rate)