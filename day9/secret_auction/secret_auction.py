import art
import os

Bidders={}

def clrscr():
    os.system('cls')

def addBidder(name,bid_price,dict):
    dict[name]=bid_price

def highBidder(bidder):
    highestBid=0
    highestBidder=""
    for name in bidder:
        if bidder[name]>highestBid:
            highestBid=bidder[name]
            highestBidder=name
    print(f"Congratulation to Mr./Mrs.{highestBidder}. He/She is the highest bidded for ${highestBid} ")




print(art.logo)
continueBid=True
while continueBid:
    name=input("Please Enter Your Name:-   ")
    bid=float(input("Please Enter Your Bid:-  "))
    addBidder(name,bid,Bidders)
    wantToContinue=input("Are there any more bidders? press y  :- ")
    if wantToContinue!='y':
        continueBid=False
    clrscr()
    
highBidder(Bidders)
