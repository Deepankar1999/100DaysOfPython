# import smtplib

# myemail="testpython193@gmail.com"
# password="aano xidx znaf tiqg"


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=myemail,password=password)
#     connection.sendmail(from_addr=myemail,
#                         to_addrs="python.test@myyahoo.com",
#                         msg="Subject:Hello\n\n This is the body")
#connection.close()




import datetime as dt
import smtplib
import random

myemail="testpython193@gmail.com"
password="aano xidx znaf tiqg"


def get_quote():
    with open("./day32/Birthday Wisher (Day 32) start/quotes.txt") as quote_file:
        all_quote=quote_file.readlines()
        quote=random.choice(all_quote)
        return quote

def send_email(myemail,password,quote):
    with smtplib.SMTP("smtp.gmail.com") as conection:
        conection.starttls()
        conection.login(user=myemail,password=password)
        conection.sendmail(from_addr=myemail,
                         to_addrs="python.test@myyahoo.com",
                         msg=f"Subject:Monday Motivation\n\n {quote}")






now=dt.datetime.now()
day=now.weekday()
if day==0:
    quote=get_quote()
    send_email(myemail,password,quote)
    
