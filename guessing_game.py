import random
import os

rando = random.randint(1, 10)
win = False
tries = 1

print("Welcome to Bert's mysterious number guessing game.\n")

guess = int(input('Please enter a number between 1 and 10: '))

while win == False:
    if guess == rando:
        print('Congratulations you have won after ' + str(tries) + ' tries!')
        win = True

    elif guess > rando:
        os.system('cls')
        tries = tries+1
        guess = int(input('Too big, please guess again: '))

    else:
        os.system('cls')
        tries = tries+1
        guess = int(input('Too small, please guess again: '))


print("Thank you for playing Bert's wacky game.\n")
print('(press any key to exit)')
input()

