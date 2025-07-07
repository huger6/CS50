from um import count


def main():
    test_lower_upper_case()
    test_middle()
    test_spaces()


def test_lower_upper_case():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks,um...") == 2

def test_middle():
    assert count("yummy") == 0

def test_spaces():
    assert count("thanks, um , for the cake.") == 1
    assert count("um?") == 1

if __name__ == "__main__":
    main()
