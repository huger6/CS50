gqol = input("What's the answer? ").lower().strip()
if gqol == str(42):
    print("Yes")

elif gqol == "forty-two":
    print("Yes")

elif gqol == "forty two":
    print("Yes")

else:
    print("No")
