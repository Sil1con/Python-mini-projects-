# Guess Number

import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def game(attempts):
    while attempts != 0:
        print(f"Number to be guessed: {rand}")
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == rand:
            print("You won! Congrats!")
            break
        elif guess < 0:
            print("The range is between 0 and 100")
            attempts -= 1
        elif guess > 100:
            print("The range is between 0 and 100")
            attempts -= 1
        elif guess > rand:
            print("Too high.")
            attempts -= 1
        elif guess < rand:
            print("Too low.")
            attempts -= 1
        else:
            print("Please, type a digit")
            attempts
        
        # Print 'Game over'
        if attempts == 0:
            print("You lose! Game over!")

stop = False

while stop != True:
    print("\n")
    rand = random.randint(0, 100)
    print("I have chosen a number between 0 and 100")
    
    difficulty = input("Choose a level of difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        game(EASY_LEVEL)
    elif difficulty == "hard":
        game(HARD_LEVEL)
    else:
        print("Please, choose a given option!")
        continue

    # Restart the game
    answer = input("Would you like to restart the game? Type 'yes' or 'no': ").lower()
    if answer == "yes":
        continue
    elif answer == "no":
        print("Bye! See you soon")
        break
    else:
        print("Unrecognizable option!")
        break