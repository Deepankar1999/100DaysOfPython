"""

"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when the ingrdients are sufficient otherwise it returns False"""
    is_enough=True
    for items in order_ingredients:
        if order_ingredients['items']>resources['items']:
            print(f"Sorry there is not enough{items}")
            is_enough=False
    return is_enough

def is_transaction_successful(money_received,drink_cost):
    """Return True when the payment is accepted,or False if the moeny is insufficient """
    if money_received>=drink_cost:
        change=round(money_received -drink_cost,2)
        print(f"Here is ${change} in change")
        global balance
        balance+=drink_cost
        return True
    else:
        print("Sorry That's Not Enough Money. Money is refunded")
        return False
def process_coins():
    """Returns the total calculations of the coins inserted"""
    print("Please Insert Coins")
    total=int(input("How many quarters? ")) * 0.25
    total+=int(input("How many dimes? ")) * 0.1
    total+=int(input("How many nickles? ")) * 0.05
    total+=int(input("How many pennies? ")) * 0.01
    return total


def make_coffee(drink_name,order_ingredients):
    """Detect the required ingredients from the resources"""
    for items in order_ingredients:
        resources[items]-=order_ingredients[items]
    print(f"Here is your {drink_name}")


balance=0

machineInOrder=True
 
while machineInOrder:
    getUserInput=input("What would you like ? \n 1. Espresso \n 2. Latte \n 3.Cappuccino ")
    if getUserInput=='off':
        machineInOrder=False
    elif getUserInput=='report':
        print(f" Water:{resources['water']}ml \n Milk:{resources['milk']}ml \n Coffee:{resources['coffee']} \n Money:${balance} ")
    else:
        drink=MENU[getUserInput]
        if is_resource_sufficient(drink['ingredients']):
            payment=process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(getUserInput,drink["ingredients"])
                
            

        
    
