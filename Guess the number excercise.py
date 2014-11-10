#Indi Knighton
#10/11/2014
#Guess the number game

import random
correct = False
random_number = random.randint(0, 100)
guesses = 0
while correct == False:
    guess = int(input("Please enter a guess between 0-100: "))
    if guesses >= 10:
        print("Sorry you've used up all of your guesses! The correct answer was {0}".format(random_number))
        correct = True
    elif guess < 0 or guess > 100:
        print("You have entered an invalid number! Please try again: ")
    elif guess > random_number:
        print("Your guess is too high! Please try again: ")
        guesses = guesses + 1
        correct = False
    elif guess < random_number:
        print("Your guess is too low! Please try again: ")
        guesses = guesses + 1
        correct = False 
    elif guess == random_number:
        print("You have correctly guessed the number in {0} guesses!".format(guesses))
        correct = True

        
        
        
            
    

 
