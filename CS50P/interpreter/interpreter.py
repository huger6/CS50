valores = input("What's the expression? ")
x, y, z = valores.split(" ")
x2 = float(x)
z2 = float(z)
if y == "+":
   result = x2 + z2
if y == "-":
   result = x2 - z2
if y == "*":
   result = x2 * z2
if y == "/":
   result = x2 / z2
print(round(result, 1))
