amount_due = 50

while amount_due > 0:
	print("Amount Due:", amount_due)
	money_inserted = int(input("Insert Coin: "))
	if money_inserted in [5, 10, 25]:
		amount_due -= money_inserted

change_owed = abs(amount_due)
print("Change Owed:", change_owed)
