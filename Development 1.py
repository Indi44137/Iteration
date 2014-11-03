#Indi Knighton
#02/11/2014
#Calculates n for a postitive integer

count = 1
total = 1
n = int(input("Please enter a positive integer: "))
for count in range(n):
    count = count + 1
    total =  2 * count
print("{0} = {1}.".format(n, total))
