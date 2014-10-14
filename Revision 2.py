#Indi Knighton
#14/10/2014
#Program asking user for a message and display the amount of times they want

message = input("Please enter your message here: ")

number = int(input("Please enter the amount of times you would to display your message: "))

if number < 0:
    print("You have entered an invalid number")
elif number >= 0:
    for count in range(number):
        print()
        print("{0}".format(message))
else:
    print("You have entered an invalid number")
    
