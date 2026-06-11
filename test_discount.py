# test_discount.py

from discount import calculate_discount


# ===== Các test cơ bản =====

def test_vip_customer():
    # Khách hàng đã là khách hàng thân thiết
    assert calculate_discount(60000000, 5000000) == 0.1


def test_normal_customer():
    # Khách hàng chưa đủ điều kiện giảm giá
    assert calculate_discount(30000000, 5000000) == 0


def test_become_vip_after_order():
    # Đơn hàng hiện tại làm tổng mua hàng đạt 50 triệu
    assert calculate_discount(45000000, 5000000) == 0.1


def test_exactly_50_million():
    # Tổng sau mua đúng bằng 50 triệu
    assert calculate_discount(49000000, 1000000) == 0.1


def test_still_not_vip():
    # Sau khi mua vẫn chưa đạt 50 triệu
    assert calculate_discount(40000000, 5000000) == 0


# ===== Test Case theo đề bài =====

def test_tc01():
    """
    Tổng trước đơn hàng: 60.000.000
    Đơn hàng hiện tại: 2.000.000
    Kỳ vọng: giảm giá 10%
    """
    assert calculate_discount(60000000, 2000000) == 0.1


def test_tc02():
    """
    Tổng trước đơn hàng: 30.000.000
    Đơn hàng hiện tại: 2.000.000
    Kỳ vọng: không giảm giá
    """
    assert calculate_discount(30000000, 2000000) == 0


def test_tc03():
    """
    Tổng trước đơn hàng: 49.000.000
    Đơn hàng hiện tại: 2.000.000
    Tổng sau mua: 51.000.000
    Kỳ vọng: giảm giá 10%
    """
    assert calculate_discount(49000000, 2000000) == 0.1