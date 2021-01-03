from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    coffee_type = input(f'Please pick your coffee {menu.get_items()} ')
    if coffee_type == 'report':
        coffee_maker.report()
        money_machine.report()
        continue
    coffee_object = menu.find_drink(coffee_type)
    if coffee_object:
        if coffee_maker.is_resource_sufficient(coffee_object):
            charge = coffee_object.cost
            print(f"That'll be ${float(coffee_object.cost)}. ")
            if money_machine.make_payment(charge):
                coffee_maker.make_coffee(coffee_object)
    else:
        continue

