dict = {}

while True:
    try:
        item = input().upper()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    except (KeyError):
        pass
    except EOFError:
        for key in sorted(dict.keys()):
            print(dict[key], key)
        break
