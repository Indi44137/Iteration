#Indi Knighton
#16/10/2014
#A program which will ask the user for a number within the range of 10-20

number = int(input("Please enter a number here: "))
if 10 >= number <= 20:
    while number <= 10 or number >= 20:
        print("You have entered an invalid number")
        number = int(input("Please enter a number here: "))
else:
    print("You have entered a number within the range")
