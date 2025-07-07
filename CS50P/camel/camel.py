camel = input("camelcase: ")
print(camel)

for letter in camel:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")
print()


