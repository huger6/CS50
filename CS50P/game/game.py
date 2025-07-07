from random import choice

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            guess_number = int(choice(range(1, n+1)))
            while True:
                guess = input("Guess: ")
                if isinstance(int(guess), int) and int(guess) > 0:
                    if int(guess) == guess_number:
                        print("Just right!")
                        break
                    elif int(guess) < guess_number:
                        print("Too small!")
                    else:
                        print("Too large!")
            break
    except ValueError:
        pass
