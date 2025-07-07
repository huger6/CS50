from plates import is_valid

def main():
    test_start_2_letters()
    test_min_max_chars()
    test_first_number_not_zero()
    test_ponctuation()
    test_numbers_middle()



def test_start_2_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False


def test_min_max_chars():
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFGH") == False


def test_first_number_not_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_ponctuation():
    assert is_valid("ANH34!") == False
    assert is_valid("ANH34.") == False
    assert is_valid("ANH34 ") == False

def test_numbers_middle():
    assert is_valid("AA22BB") == False
    assert is_valid("AABB22") == True
