#Indi Knighton
#16/10/2014
#Asks the user for the amount of numbers they want to average and then the numbers

total = 0
counter = 1
import math
input_average = float(input("Please enter the amount of numbers you want to be averaged: "))
print()
while counter <= input_average:
    print()
    number = float(input("Please enter an number here: "))
    total = total + number
    counter = counter + 1
total = total / input_average
print()
print("The average of the numbers is {0}".format(total))
    
#I have used float instead of int so that you can calculate decimal answers as well
