import sys


def main():
    lines = get_file()
    number_of_lines = 0
    for line in lines:
        if line.lstrip().startswith("#"):
            continue
        elif line.strip() == "":
            continue
        else:
            number_of_lines += 1
    print(number_of_lines)


def get_file():
    if len(sys.argv) == 2:
        try:
            if sys.argv[1].endswith(".py"):
                with open(sys.argv[1]) as file:
                    return file.readlines()
            else:
                sys.exit("Not a Python file")
        except FileNotFoundError:
            sys.exit("File does not exist")

    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
