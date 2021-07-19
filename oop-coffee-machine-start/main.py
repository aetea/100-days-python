from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_running = True
while is_running:
    order = input(f"What would you like? ({menu.get_items()}): ")

    if order == "off":
        is_running = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order_item = menu.find_drink(order)

        if order_item == None:
            continue

        can_make = coffee_maker.is_resource_sufficient(order_item)
        paid = money_machine.make_payment(order_item.cost)

        if can_make and paid:
            coffee_maker.make_coffee(order_item)
