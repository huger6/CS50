def main():
    text = input("How much fuel is in the tank? ")
    tank = convert(text)
    final_result = gauge(tank)
    print(final_result)


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            if int(y) >= int(x):
                fuel = (int(x) / int(y)) * 100
                return round(fuel)
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        alpha = percentage
        return str(alpha) + "%"


if __name__ == "__main__":
    main()
