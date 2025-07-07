from validator_collection import validators, checkers, errors

def main():
    email_adress = input("Email: ")
    try:
        check_email = validators.email(email_adress)
        print("Valid")
    except ValueError:
        print("Invalid")
    except errors.EmptyValueError:
        print("Invalid")
    except errors.InvalidEmailError:
        print("Invalid")


if __name__ == "__main__":
    main()


