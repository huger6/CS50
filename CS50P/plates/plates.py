def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
     if len(s) >= 2 and len(s) <= 6:
        if s.isalpha():
            return True
        elif s.isalnum() and s[0:2].isalpha():
            for chars in s:
                if chars.isdigit():
                    position = s.index(chars)
                    if s[position:].isdigit() and int(chars) != 0:
                        return True
                    else:
                        return False
        elif s.isalnum():
            return False



if __name__ == "__main__":
    main()

