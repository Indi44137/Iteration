#Indi Knighton
#02/11/2014
#A program to paste a row of stars depending on the user input

number_of_rows = int(input("Please enter the amount of rows: "))
number_of_stars = int(input("Please enter the amount of stars per row: "))
for count in range(number_of_rows):
    stars = number_of_stars * "*"
    print(stars)
    
