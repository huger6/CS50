def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    d = float(dollars.replace("$",""))
    return d


def percent_to_float(percent):
    p = float(percent.replace("%",""))
    p2 = p / 100
    return p2


main()
