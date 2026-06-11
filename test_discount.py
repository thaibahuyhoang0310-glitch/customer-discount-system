# test_discount.py

from discount import calculate_discount


# ===== Các test cơ bản =====

def test_vip_customer():
    # Khách hàng đã là khách hàng thân thiết
    assert calculate_discount(60000000, 5000000) == 0.1


def test_normal_customer():
    # Khách hàng chưa đủ điều kiện giảm giá
    assert calculate_discount(30000000, 5000000) == 0

# ===== Test Case theo đề bài =====

def test_tc01():
    assert calculate_discount(60000000, 2000000) == 0.1


def test_tc02():
    assert calculate_discount(30000000, 2000000) == 0


def test_tc03():
    assert calculate_discount(49000000, 2000000) == 0.1