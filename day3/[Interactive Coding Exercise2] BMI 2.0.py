# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi=weight/height**2
bmi=round(bmi)
if bmi<=18.5:
    print(f"Your BMI is {bmi} you are:- Underweight")
elif bmi>18.5 and bmi<=25:
    print(f"Your BMI is {bmi} you are:- Normal Weight")
elif bmi>25 and bmi<=30:
    print(f"Your BMI is {bmi} you are:- Slightly Overweight")
elif bmi>30 and bmi<=35:
    print(f"Your BMI is {bmi} you are:- Obese")
elif bmi>35:
    print(f"Your BMI is {bmi} you are:- Clinically Obese")
