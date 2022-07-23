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

money = 0.0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def start(resources: list):
    while True:
        response: str = input("What would you like? (espresso/latte/cappuccino): ")

        if response  == "off":
            break
        elif response == "report":
            report()
        else:
            drink = MENU[response]
            if in_stock(drink["ingredients"]):
                payment = process_coins()
                if valid_amount(payment, drink["cost"]):
                    process_drink(response, drink["ingredients"])


def in_stock(ingredients: list):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
            
    return True

def process_coins():
    print("Insert coins.")
    total = float(input("Quarters: ")) * 0.25
    total += float(input("Dimes: ")) * 0.10
    total += float(input("Nickels: ")) * 0.05
    total += float(input("Pennies: ")) * 0.01

    return total


def valid_amount(payment: float, cost: float):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


def process_drink(name: str, ingredients: list):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {name}. Enjoy!")


def report():
    global money
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


start()