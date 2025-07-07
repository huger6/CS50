def main():
    prompt = input()
    result = convert(prompt)
    print(result)

def convert(prompt):
    prompt2 = prompt.replace(":(","🙁").replace(":)","🙂")
    return prompt2

main()
