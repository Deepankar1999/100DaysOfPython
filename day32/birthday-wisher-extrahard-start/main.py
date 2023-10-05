##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as pd
import random
import smtplib

myemail="testpython193@gmail.com"
password="aano xidx znaf tiqg"

def check_date(today_day,month):
    current_time=dt.datetime.now()
    if today_day==current_time.day and month==current_time.month:
        return True
    else:
        return False

def get_random_letter():
    file_location=["./day32/birthday-wisher-extrahard-start/letter_templates/letter_1.txt",
                   "./day32/birthday-wisher-extrahard-start/letter_templates/letter_2.txt",
                   "./day32/birthday-wisher-extrahard-start/letter_templates/letter_3.txt"
                   ]
    return random.choice(file_location)

def send_greetings(message,email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myemail,password=password)
        connection.sendmail(from_addr=myemail,
                            to_addrs=email,
                            msg=f"Subject: Happy Birthday\n\n {message}"
                            )

df=pd.read_csv("./day32/birthday-wisher-extrahard-start/birthdays.csv")
df=df.to_dict('index')


for key in df:
    name,email,month,day=df[key]['name'],df[key]['email'],df[key]['month'],df[key]['day']
    if check_date(day,month):
        letter_location=get_random_letter()
        with open(letter_location) as file:
            letter=file.read()
        letter=letter.replace("[NAME]",name)
        send_greetings(letter,email)

        

        
