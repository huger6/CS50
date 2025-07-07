from tabulate import tabulate
import csv
import sys

def main():
    reader = get_input()
    info = []
    headers = None
    for row in reader:
        if not headers:
            headers = list(row.keys())
        info.append(row.values())
    print(tabulate(info,headers = headers, tablefmt="grid"))


def get_input():
    if len(sys.argv) == 2:
        try:
            if sys.argv[1].endswith(".csv"):
                file = open(sys.argv[1])
                return csv.DictReader(file)
            else:
                sys.exit("Not a CSV file")
        except FileNotFoundError:
            sys.exit("File does not exist")

    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
