#TODO 1:- Create a function to Generate A Random Number
#TODO 2:- Let Player Choose between Easy and Hard Mode
#TODO 3:- Create Variables UserLife
#TODO 4:-Create Function that check the user's guess with randomly generated number, run till lives are over or user wins

import random

GameWon=False
numberGenerated=random.randint(1,100)
difficulty=input("Welcome to the number guessing game! \n I'm thinking of a number between 1 and 100.\n Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty=='easy':
    PlayerLife=10
elif difficulty=='hard':
    PlayerLife=5

userGuess=int(input("Enter Your Guess: "))
while PlayerLife!=0 and not GameWon:
    if numberGenerated==userGuess:
        GameWon=True
        print("You Won")
    elif numberGenerated<userGuess:
        PlayerLife-=1
        print(f"You have {PlayerLife} Chances The number is too high")
        userGuess=int(input("Guess Again "))
    elif numberGenerated>userGuess:
        PlayerLife-=1
        print(f"You have {PlayerLife} Chances The number is too low")
        userGuess=int(input("Guess Again "))
if PlayerLife==0:
    print("You have lost all lives")
