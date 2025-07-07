from bank import value

def main():
    test_hellos()
    test_hs()
    test_middle_hs()

def test_hellos():
    assert value("hello") == 0
    assert value("Hello, someone") == 0
def test_hs():
    assert value("hey") == 20
    assert value("H") == 20
def test_middle_hs():
    assert value("what's cracking?") == 100
    assert value("What's Hovering?") == 100

if __name__ == "__main__":
    main()
