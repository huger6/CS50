def main():
    text = input("Text: ")
    print(shorten(text))


def shorten(word):
    output = ""
    for letter in word:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            output += letter
    return output


if __name__ == "__main__":
    main()
