from app import add_numbers

def test_addition_correct():
    assert add_numbers(2, 3) == 5

def test_addition_negative():
    assert add_numbers(-1, 1) == 0
