from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    print(f"Hello, the available options are {menu.get_items()}.")
    drink = input("What type of coffee would you like to order?: ")
    if drink == "end":
        break
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)




