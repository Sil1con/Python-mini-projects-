benefit = 0

coins = {
    "quarters": {
        "value": 0.25,
        "amount": 0
    },
    "dimes": {
        "value": 0.10,
        "amount": 0
    },
    "nickles": {
        "value": 0.05,
        "amount": 0
    },
    "pennies": {
        "value": 0.01,
        "amount": 0
    }
}

tank = {
    "water": 1000,
    "milk": 500,
    "coffee": 200
}

MENU = {
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    }
}


def report():
    print("\nReport:")
    print(f"    Benefit: ${benefit}")
    for item in tank:
        print(f"{item} = {tank[item]} ml.")


def fill_tank():
    global tank
    tank = {
        "water": 1000,
        "milk": 500,
        "coffee": 200
    }
    print("The tank has been filled")


def menu():
    print("\nCoffee selection:")
    for coffee in MENU:
        print(f"    {coffee}: ${MENU[coffee]["cost"]}")


def enough_resources(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        value = MENU[coffee]["ingredients"][ingredient]
        if tank[ingredient] < value:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def enough_money(coffee, money):
    cost = MENU[coffee]["cost"]
    if money < cost:
        print(f"{money} and {cost}")
        return False
    else:
        return True


def insert_coins():
    money = 0
    print("Please, insert coins.")
    for item in coins:
        coin = coins[item]
        coin_value = coin["value"]
        amount = int(input(f"How many {item}?: "))
        coin["amount"] = amount
        money += float(coin_value * amount)
    return money


def return_rest(coffee, money):
    money -= MENU[coffee]["cost"]
    print(f"Here is your rest: ${money}")


def make_coffee(coffee):
    global benefit
    for ingredient in MENU[coffee]["ingredients"]:
        value = MENU[coffee]["ingredients"][ingredient]
        tank[ingredient] -= value
    print(f"Here you are! Enjoy your {coffee}!")


# Global variables
active = True
money = 0

while active is True:
    menu()
    money += insert_coins()
    coffee = input("What would you like? ").lower()
    if coffee == "stop":
        print("See you soon! Bye")
        break
    elif coffee == "report":
        report()
    elif coffee == "fill":
        fill_tank()
    elif coffee not in MENU:
        print("Please, select an appropriate option")
        continue
    else:
        if enough_resources(coffee) == False:
            continue
        else:
            price = MENU[coffee]["cost"]
            if enough_money(coffee, money) == False:
                print("You do not have enough money")
                continue
            else:
                benefit += MENU[coffee]["cost"]
                return_rest(coffee, money)
                make_coffee(coffee)
                continue
