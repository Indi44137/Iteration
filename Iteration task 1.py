#Indi Knighton
#14/10/2014
#program to prompt for 8 numbers and report the total to the user


total = 0
counter = 0

for counter in range(1,9):
    print()
    number = int(input("Please enter number {0} in the series: ".format(counter)))
    total = total + number
    counter = counter + 1
print("The total is {0}".format(total))
