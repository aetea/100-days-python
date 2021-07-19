# ======= DRINK COFFEE ==========

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


def check_resources(order):
    """Check if machine has enough resources for user's order."""
    needed = MENU[order]["ingredients"]
    for ingr in needed:
        if needed[ingr] > resources[ingr]:
            print(f"Sorry, there is not enough {ingr}.")
            return False
        else:
            return True


def process_coins():
    """Prompt user for coins after drink was chosen, then calculate and return 
    total."""
    print("Please insert coins.")
    # TODO validate num_coins (ints only)
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + \
        (nickels * 0.05) + (pennies * 0.01)

    return total


def validate_payment(amt_paid):
    """Check if transaction is valid, then issue change or update balance and 
    return true/false."""
    order_cost = MENU[order]["cost"]

    if amt_paid < order_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    elif amt_paid > order_cost:
        change_to_give = amt_paid - order_cost
        change_to_give = round(change_to_give, 2)
        print(f"Here is ${change_to_give} in change.")

    resources["money"] = resources.get("money", 0) + order_cost
    return True


def make_coffee():
    """Update resources to make drink and show user confirmation."""
    needed = MENU[order]["ingredients"]
    for ingr in needed:
        resources[ingr] -= needed[ingr]
    print(f"Here is your {order} ☕️ Enjoy!")


def report():
    """Print remaining resources from dictionary."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources.get('money', 0)}")
    # for key, value in resources.items():
    #     print(f"{key.title()}: {value}ml")


# ================  MAIN FUNCTION ==============

print("Hello! It's a good time for a pick-me-up.")

# prompt user for drink
while True:
    print()
    order = input("What would you like? (espresso/latte/cappuccino): ")
    order = order.lower()

    # admin controls: turn off / show remaining resources
    if order == "off":
        break

    elif order == "report":
        report()
        continue

    elif order not in ["espresso", "latte", "cappuccino"]:
        print("Sorry, we don't have that. Please try again.")
        continue

    # attempt coffee transaction

    # -- first, check if machine has enough resources
    is_machine_ok = check_resources(order)

    # -- if yes, move on to payment
    if is_machine_ok == True:
        amt_paid = process_coins()
    else:
        continue

    if validate_payment(amt_paid) == True:
        make_coffee()
    else:
        continue
