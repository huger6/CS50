import csv
import sys

def main():
    reader, after = get_input_and_open()
    output = []
    for names in reader:
        last, first = names["name"].split(",")
        house = names["house"]
        output.append({"first": first.lstrip(),"last": last, "house": house })


    with open(after, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row["first"],"last": row["last"], "house": row["house"]})


def get_input_and_open():
    if len(sys.argv) == 3:
        try:
            if sys.argv[1].endswith(".csv"):
                try:
                    if sys.argv[2].endswith(".csv"):
                        file = open(sys.argv[1])
                        reader = csv.DictReader(file)
                        after = sys.argv[2]
                        return reader, after
                except FileNotFoundError:
                    pass
            else:
                sys.exit("Not a CSV file")
        except FileNotFoundError:
            sys.exit("File does not exist")

    elif len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
