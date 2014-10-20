#Indi Knighton
#20/10/2014
#A program asking the user for a series of numbers and a rogue value and print the average of the numbers

result = 0
total = 0
for result in range(0,5):
    result = int(input("Please enter a number here: "))
    if result >= 0:
        total = total + result
    elif result < 0:
        result = int(input("Please enter a number here: "))             
average = total / 5
print("The average is {0}".format(average))
    
