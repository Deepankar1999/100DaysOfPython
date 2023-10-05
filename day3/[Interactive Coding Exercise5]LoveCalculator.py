# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1=name1.lower()
name2=name2.lower()
name=name1+name2

l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')

t=name.count('t')
r=name.count('r')
u=name.count('u')


trueVal=t+r+u+e
loveVal=l+o+v+e

totalScore=str(trueVal) +str(loveVal)
totalScore=int(totalScore)
if totalScore<=10 or totalScore>=90:
    print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif totalScore>=40 and totalScore<=50:
    print(f"Your score is {totalScore}, you are alright together.")
else:
    print(f"Your score is {totalScore}.")
