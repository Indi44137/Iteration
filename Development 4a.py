invalid = True
print("Please enter -1 when you have entered all of your numbers!")
biggest=0
while invalid:
	number = int(input("Please enter a number here: "))
	if biggest == 0:
		biggest=number
	elif biggest<number:
		biggest=number
	if number == -1:
		print("The largest number you have entered is {0}!".format(biggest))
		invalid = False
