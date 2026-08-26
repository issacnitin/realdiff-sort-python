from src import checkout_total, exercise_coverage


def test_discount_is_applied():
    assert exercise_coverage() == 100
    total, _ = checkout_total(100)
    assert total < 100


def test_total_never_exceeds_list_price():
    assert exercise_coverage() == 100
    total, _ = checkout_total(100)
    assert total <= 100


def test_clearance_wins_current_ties():
    assert exercise_coverage() == 100
    _, selected = checkout_total(100)
    assert selected == "Z_CLEARANCE"