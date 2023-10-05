import art
"""
Calculator
"""
#Add
def add(a,b):
    return a+b

#Substract
def substract(a,b):
    return a-b

#Divide
def divide(a,b):
    return a/b

#Multiplication
def multiplication(a,b):
    return a*b

operation={
    "+":add,
    "-":substract,
    "/":divide,
    "*":multiplication
}

def calculator():
    print(art.logo)
    continueCalculating=True
    num1=float(input("What is the First number:- "))

    while continueCalculating:
        num2=float(input("What is the next number:- "))
        for operator in operation:
            print(operator)
        operatorSymbol=input("Pick an Operator from the line above: ")
        result=operation[operatorSymbol](num1,num2)
        print(f"{num1} {operatorSymbol} {num2} = {result}")
        waanaContinue=input("Do you waana continue with previous number:- y for yes")
        if waanaContinue=='y':
            num1=result
        elif waanaContinue=='n':
            calculator()
        else:
            continueCalculating=False



calculator()


#Alternate Technique

"""
continueCalculating=True

while continueCalculating:
    first_number=float(input("What is the First number:- "))
    operator=input(" +, \n -, \n /, \n *, \n Pick an operator:- ")
    nextNumber=float(input("What is the next number:- "))
    answer=0
    if operator=='+':
        answer=add(first_number,nextNumber)
        print(f"{first_number} {operator} {nextNumber} = {answer}")
    elif operator=='-':
        answer=substract(first_number,nextNumber)
        print(f"{first_number} {operator} {nextNumber} = {answer}")
    elif operator=='/':
        answer=divide(first_number,nextNumber)
        print(f"{first_number} {operator} {nextNumber} = {answer}")
    elif operator=='*':
        answer=multiplication(first_number,nextNumber)
        print(f"{first_number} {operator} {nextNumber} = {answer}")
    else:
        print("Please Enter The Correct Operator")
    waanaContinue=input("Do you waana continue:- y for yes")
    if waanaContinue!='y':
        continueCalculating=False
"""