x = input("File name: ").lower().strip()
if x.endswith(".gif") == True:
    print("image/gif")
elif x.endswith(".jpg") == True:
    print("image/jpeg")
elif x.endswith(".jpeg") == True:
    print("image/jpeg")
elif x.endswith(".png") == True:
    print("image/png")
elif x.endswith(".pdf") == True:
    print("application/pdf")
elif x.endswith(".txt") == True:
    print("text/plain")
elif x.endswith(".zip") == True:
    print("application/zip")
else:
    print("application/octet-stream")

