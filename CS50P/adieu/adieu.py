import inflect

list = []
def main():
	while True:
		try:
			name = input("Name: ")
			list.append(name)
		except EOFError:
			names_v2 = format_list(list)
			print("Adieu, adieu, to " + str(names_v2))
			break

def format_list(x):
	if len(x) == 1:
		return x[0]
	elif len(x) == 2:
		return " and ".join(x)
	else:
		return ", ".join(x[:-1]) + ", and " + x[-1]

if __name__ == "__main__":
	main()
