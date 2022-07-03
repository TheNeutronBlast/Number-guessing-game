import random

print("Number Guessing game")
number = random.randint(1,9)
chance = 0
print("Guess a number between 1 and 9")
while chance<3:
    guess = int(input("enter your guess:"))

    if number == guess:
        print("yay you guessed it correctly now try again so you fail.")

    elif number > guess:
        print("Too low looser")

    else: print("Too high looser")

    chance+=1