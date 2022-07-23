MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


# TODO: 1. Prompt user for input

def start(resources: list):
    money = 0.0
    while True:
        response: str = input("What would you like? (espresso/latte/cappuccino): ")

        if response == "espresso":
            money, resources = process('espresso', resources, money)
        elif response == "latte":
            money, resources = process('latte', resources, money)
        elif response == "cappuccino":
            money, resources = process('cappuccino', resources, money)
        elif response == "report":
            report(money)
        elif response == "off":
            break


def process(name: str, sources: list, funds: float):

    stock_flag, missing = in_stock(name, sources)

    if stock_flag != True:
        print(f"Sorry there is not enough {missing}")
    else:
        funds_flag, funds = process_coins(name, funds)
        if funds_flag:
            sources = process_drink(name, sources)
            print("Here is your latte. Enjoy!")
    
    return funds, sources


def in_stock(name: str, sources: list):
    for k, v in MENU[name]['ingredients'].items():
        if sources[k] < v:
            return False, k
            
    return True, ""


def process_coins(name: str, funds: str):
    change = 0.0

    print("Insert coins:")
    quarters = float(input("Quarters: ")) * 0.25
    dimes = float(input("Dimes: ")) * 0.10
    nickles = float(input("Nickels: ")) * 0.05
    pennies = float(input("Pennies: ")) * 0.01

    total = quarters + dimes + nickles + pennies

    if total < MENU[name]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > MENU[name]["cost"]:
        change = total - MENU[name]["cost"]
        funds += MENU[name]["cost"]
        print(f"Here is ${change} dollars in change.")
    else:
        funds += MENU[name]["cost"]
    
    return True, funds


def process_drink(name: str, sources: list):
    for k, v in MENU[name]['ingredients'].items():
        sources[k] -= v

    return sources


def report(funds: float):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${funds}")

if __name__ == "__main__":
    start(resources)
# print(MENU['espresso']['ingredients']['water'])
#in_stock("espresso", resources)