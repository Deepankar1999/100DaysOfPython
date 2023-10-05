# Get Random Question from game data
# Print the data in questionable format
#Take User Input
#check for user's answer
#Store the score and print it

import random 
from art import logo,vs
import gamedata

CURRENT_SCORE=0

def randomQuestion():
    option=random.choice(gamedata.data)

    return option

def showOption(optionA,optionB):
    print(logo)
    print(f"Option A : {optionA['name']} , {optionA['description']}, from {optionA['country']}")
    print(vs)
    print(f"Option B : {optionB['name']} , {optionB['description']}, from {optionB['country']}")

def choiceComparison(optionA,optionB,user_choice):

    if user_choice=='a':
        global CURRENT_SCORE
        if optionA['follower_count']>optionB['follower_count']:
            CURRENT_SCORE+=1
            print(f"You're right ! Current Score: {CURRENT_SCORE}")
            return True
            
        else:
            print(f"Sorry That's A wrong Answer ! Current Score: {CURRENT_SCORE}")
            return False
            
    else:
        if optionB['follower_count']>optionA['follower_count']:
            CURRENT_SCORE+=1
            print(f"You're right ! Current Score: {CURRENT_SCORE}")
            return True
            
        else:
            print(f"Sorry That's A wrong Answer ! Current Score: {CURRENT_SCORE}")
            return False

optionA=randomQuestion()
optionB=randomQuestion()
while optionA==optionB:
    optionB=randomQuestion()

gameStatus=True

while gameStatus:
    showOption(optionA,optionB)

    user_choice=input("Who has more followers? Type 'A' or 'B'").lower()
    gameStatus=choiceComparison(optionA,optionB,user_choice)
    optionA=optionB
    optionB=randomQuestion()


