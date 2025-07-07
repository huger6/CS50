import random


def main():
    level = get_level()
    questions = 0
    score = 0
    while questions < 10:
        x, y = generate_integer(level)
        number_of_tries = 0
        while number_of_tries < 3:
            result = input(f"{x} + {y} = ")
            if int(result) == int(x + y):
                score += 1
                questions += 1
                break
            else:
                print("EEE")
                number_of_tries += 1
                if number_of_tries == 3:
                    print(f"{x} + {y} = {int(x+y)}")
                    questions += 1
                    break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    else:
        raise ValueError
    return x, y

if __name__ == "__main__":
    main()
