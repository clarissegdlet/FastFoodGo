from fastfoodgo.order import calculate_order_total


def test_calculate_order_total_nominal():
    items = [
        {"price": 10, "quantity": 2},
        {"price": 5, "quantity": 1}
    ]
    assert calculate_order_total(items) == 25


def test_calculate_order_total_empty():
    items = []
    assert calculate_order_total(items) == 0
