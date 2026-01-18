from fastfoodgo.status import is_valid_status_transition


def test_valid_status_transition():
    assert is_valid_status_transition("CREATED", "PAID") is True


def test_invalid_status_transition():
    assert is_valid_status_transition("PAID", "CREATED") is False


def test_final_status_transition():
    assert is_valid_status_transition("DELIVERED", "PAID") is False
