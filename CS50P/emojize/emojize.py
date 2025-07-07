import emoji

while True:
    answer = input("Input: ")
    try:
        print("Output: ", emoji.emojize(answer, language='alias'))
        break
    except:
        pass


