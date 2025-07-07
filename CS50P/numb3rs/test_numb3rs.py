from numb3rs import validate
from pytest import raises


def main():
    test_format()
    test_range()


def test_range():
    assert validate(rf"0.0.0.0") == True
    assert validate(rf"255.255.255.255") == True
    assert validate(rf"144.50.1.245") == True
    assert validate(rf"1.256.1.2") == False
    assert validate(rf"500.5.0.5") == False
    assert validate(rf"1000.1000.1000.1000") == False
    assert validate(rf"257.30.300.146") == False


def test_format():
    assert validate(rf"1.2.3.4") == True
    assert validate(rf"8.8.8") == False
    assert validate(rf"6") == False
    assert validate(rf"1.1") == False
    assert validate(rf"244.244.244.244.244") == False


if __name__ == "__main__":
    main()
