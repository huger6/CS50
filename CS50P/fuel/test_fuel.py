from fuel import convert
from fuel import gauge
from pytest import raises

def main():
    test_zero_division()
    test_value_error()
    test_empty_output()
    test_full_output()
    test_middle_output()
    test_gauge_function()


def test_zero_division():
    with raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with raises(ValueError):
        convert("cat/dog")


def test_empty_output():
    assert convert("0/100") == 0
    assert convert("1/100") == 1


def test_full_output():
    assert convert("100/100") == 100
    assert convert("99/100") == 99


def test_middle_output():
    assert convert("1/4") == 25
    assert convert("5/10") == 50
    assert convert("98/100") == 98


def test_gauge_function():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(51) == "51%"


if __name__ == "__main__":
    main()

