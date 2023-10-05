rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
CompChoice=random.choice([1,2,3])

UserChoice=int(input("Please Enter Your Choice:= 1 for Rock;  2 for Paper; 3 for scissors"))



if UserChoice == 1:
    print(f"User Choice is {rock}")
    if CompChoice ==1:
        print(f"Computer choice is { rock}")
        print("It's a draw")
    elif CompChoice ==2:
        print(f"Computer choice is { paper}")
        print("It's Computer's Victory")
    elif CompChoice ==3:
        print(f"Computer choice is { scissors}")
        print("It's User's victory")
elif UserChoice == 2:
    print(f"User Choice is {paper}")
    if CompChoice ==1:
        print(f"Computer choice is { rock}")
        print("  It's User's victory")
    elif CompChoice ==2:
        print(f"Computer choice is { paper}")
        print("It's a draw")
    elif CompChoice ==3:
        print(f"Computer choice is { scissors}")
        print("It's Computer's Victory")
elif UserChoice == 3:
    print(f"User Choice is {scissors}")
    if CompChoice ==1:
        print(f"Computer choice is { rock}")
        print("It's Computer's Victory ")
    elif CompChoice ==2:
        print(f"Computer choice is { paper}")
        print("It's User's victory")
    elif CompChoice ==3:
        print(f"Computer choice is { scissors}")
        print(" It's a draw")
