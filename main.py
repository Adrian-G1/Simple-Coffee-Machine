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

money: float = 0.0


# TODO: 1. Prompt user for input

def start():
    while True:
        response: str = input("What would you like? (espresso/latte/cappuccino): ")

        if response == "espresso":
            pass
        elif response == "latte":
            pass
        elif response == "cappuccino":
            pass
        elif response == "report":
            report()
        elif response == "off":
            break


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def drink(name: str, sources: list):
    for k, v in MENU[name]['ingredients'].items():
        print(f"{k.capitalize()}, {v}")
        if sources[k] >= v:
            print(k)


#start()
# print(MENU['espresso']['ingredients']['water'])
drink("espresso", resources)