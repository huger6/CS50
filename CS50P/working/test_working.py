from working import convert
from working import convert_format
from pytest import raises


def main():
    test_format()
    test_convert_format()
    test_wrong_hour()
    test_wrong_minute()


def test_format():
    assert convert("09:00 AM to 05:00 PM") == ("09", ":00", "AM", "05", ":00", "PM")
    assert convert("9 AM to 5 PM") == ("9", None, "AM", "5", None, "PM")
    assert convert("09:00 PM to 05:00 AM") == ("09", ":00", "PM", "05", ":00", "AM")
    assert convert("09:00 AM to 05:00 PM") == ("09", ":00", "AM", "05", ":00", "PM")
    assert convert("9:60 AM to 5:00 PM") == ValueError
    assert convert("9 AM - 5 PM") == ValueError
    assert convert("09:00 AM - 17:00") == ValueError


def test_convert_format():
    assert convert_format("9", None, "AM") == "09:00"
    assert convert_format("5", None, "PM") == "17:00"
    assert convert_format("11", ":30", "AM") == "11:30"
    assert convert_format("2", ":45", "PM") == "14:45"
    assert convert_format("12", ":00", "AM") == "00:00"
    assert convert_format("12", ":00", "PM") == "12:00"
    assert convert_format("7", None, "PM") == "19:00"
    assert convert_format("8", None, "AM") == "08:00"
    assert convert_format("10", ":15", "PM") == "22:15"
    assert convert_format("4", ":05", "AM") == "04:05"


def test_wrong_hour():
    with raises(ValueError):
        convert("13 PM to 17 PM")

def test_wrong_minute():
    with raises(ValueError):
        convert("09:60 AM to 06:60 PM")

if __name__ == "__main__":
    main()


#não passa no check50 porque eu fiz a função convert de forma diferente, mas verifica na mesma todas as condições do problema
