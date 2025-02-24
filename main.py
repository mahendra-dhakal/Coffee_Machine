from menu import Menu , MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#creating objects

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

while True:
    options=menu.get_items()
    user_choice=input(f"What would you like?:{options}")
    
    
    if user_choice=='off':
        break
    elif user_choice=='report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(user_choice)
        check=coffee_maker.is_resource_sufficient(drink)
        if check:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                
            


   