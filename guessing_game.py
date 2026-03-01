import random
import os

rando = random.randint(1, 10) #generate a random number the user will then need to guess
win = False #pre-set the while condition to make sure it runs through at least one time
tries = 1 #track how many guesses the user has entered

print("Welcome to Bert's mysterious number guessing game.\n")

guess = int(input('Please enter a number between 1 and 10: ')) #accept the users initial guess

while win == False: 
    if guess == rando: #if the users guess matches the games secret random number roll, print the winning message and number of tries
        print('Congratulations you have won after ' + str(tries) + ' tries!') #use str(tries) to convert tries from an integer to a string type for printing
        win = True #switch the flag status to exit the while loop

    elif guess > rando:
        os.system('cls') #clear the screen of previous guesses 
        tries = tries+1 #increment the number of guesses taken by the player
        guess = int(input('Too big, please guess again: '))

    else:
        os.system('cls') #clear the screen of previous guesses 
        tries = tries+1 #increment the number of guesses taken by the player
        guess = int(input('Too small, please guess again: '))


print("Thank you for playing Bert's wacky game.\n")
print('(press the Enter key to exit)')
input()

