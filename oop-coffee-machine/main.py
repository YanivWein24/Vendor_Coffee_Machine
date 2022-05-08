from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo


def main():
    admin_password = "1234"  # used in refill()

    # Create an object for each class we will use
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    print(logo)
    print("Welcome!\n\n")
    print(
        "You can type:\n\n"
        "* menu -  to see the menu\n"
        "* report -  to check for quantities of the ingredients\n"
        "* refill -  to restock on ingredients\n"
        "* off -  to turn off the machine"
    )

    while True:
        order = input(
            "\nWhat would you like to order?: espresso/latte/cappuccino/americano: "
        ).lower()
        if order == "menu":
            menu.print_items()
        elif order == "off":
            print("Goodbye!")
            break
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        elif order == "refill":
            coffee_maker.resources = coffee_maker.refill(admin_password)
        else:
            drink = menu.find_drink(order)
            # find_drink() returns the drink in a MenuItem object if typed correctly, or else returns None
            if (
                drink != None
                and coffee_maker.is_resource_sufficient(drink)
                and money_machine.make_payment(drink.cost)
            ):
                coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
