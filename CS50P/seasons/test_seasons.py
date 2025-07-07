from seasons import Minutes

def main():
    test_invalid_format()


def test_invalid_format():
    assert Minutes.isvalid(Minutes, "2006-09-25") == True
    assert Minutes.isvalid(Minutes, "2006-9-3") == False
    assert Minutes.isvalid(Minutes, "September 25, 2006") == False


if __name__ == "__main__":
    main()
