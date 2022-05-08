from art import logo
from prettytable import PrettyTable


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
    },
    "americano": {
        "ingredients": {
            "water": 300,
            "coffee": 26,
        },
        "cost": 2.0,
    },
}

coins = {"quarters": 0.25, "dimes": 0.1, "nickles": 0.05, "pennies": 0.01}

global money
money = 0


def report(resources):
    """Prints a table containing the Machine's stock and total cash"""
    report_table = PrettyTable()
    report_table.add_column("Resource", ["Water", "Milk", "Coffee", "Money"])
    report_table.add_column(
        "Amount",
        [
            f"{resources['water']}ml\n",
            f"{resources['milk']}ml\n",
            f"{resources['coffee']}gr\n",
            f"${money}",
        ],
    )
    print("\n")
    print(report_table)


def check_resources(resources, order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry..\nNot enough {item} ")
            return False
    return True


def refill(resources):
    """Receives the Machine's resources. Returns a full stock if stock is not full"""
    full_resources = {
        "water": 600,
        "milk": 250,
        "coffee": 100,
    }
    if resources == full_resources:
        print("\n* Stock already full *")
        return resources
    else:
        while True:
            confirmation = input(
                "\nTo continue, please enter the administrator password: "
            ).lower()
            if confirmation == "2402":
                print("\n* Stock refilled! *")
                return full_resources
                # break
            elif confirmation == "q":
                print("\n* Process Canceled *")
                break
            else:
                print("\nPlease enter the correct password, or type 'q' to cancel")


def count_coins(coins, cost):
    """Receives the types of coins, and the cost of the drink. Returns the total value of the coins in integer"""
    print(f"\nThis drink cost: ${cost}\n")
    while True:
        try:
            print("Please insert coins: \n")
            qur = int(input("how many quarters?: ")) * coins["quarters"]
            dim = int(input("how many dimes?: ")) * coins["dimes"]
            nic = int(input("how many nickles?: ")) * coins["nickles"]
            pen = int(input("how many pennis?: ")) * coins["pennies"]
            sum = qur + dim + nic + pen
            print(f"\nYou inserted ${round(sum,2)} in total.")
            break
        except:
            print("* Please use numbers only *")
            continue
    return sum


def is_money_enough(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received < drink_cost:
        print("Sorry not enough money...\nMoney refunded")
        return False
    elif money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if money_received > drink_cost:  # print only if money_received != drink_cost
            print(f"This is your change: ${change}")
        global money
        money += drink_cost
        return True


def make_coffee(resources, drink_name, ingredients):
    """Reduces the amount of ingredients from the machine's resources. Serving the coffee"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!\n")


def menu(menu):
    """Prints a table containing all coffee types, ingredients and costs"""
    table = PrettyTable()
    all_coffee_ingredients = [
        "Water: 50ml\nCoffee: 18gr",
        "Water: 200ml\nMilk: 150ml\nCoffee: 24gr",
        "Water: 250ml\nMilk: 100ml\nCoffee: 24gr",
        "Water: 300ml\nCoffee: 26gr",
    ]
    table.add_column(
        "Coffee",
        ["Espresso\n\n\n", "Latte\n\n\n\n", "Cappuccino\n\n\n\n", "Americano\n\n\n"],
    )
    table.add_column("Ingredients", all_coffee_ingredients)
    table.add_column("Cost", ["$ 1.5", "$ 2.5", "$ 3.0", "$ 2.0"])
    table.align = "l"
    print("\n")
    print(table)


def main():
    resources = {
        "water": 600,
        "milk": 250,
        "coffee": 100,
    }

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
            menu(MENU)
        elif order == "off":
            print("Goodbye!")
            break
        elif order == "report":
            report(resources)
        elif order == "refill":
            resources = refill(resources)
        elif (
            order != "espresso"
            and order != "latte"
            and order != "cappuccino"
            and order != "americano"
        ):
            print("please type correctly")
        else:
            drink = MENU[order]
            if check_resources(resources, drink["ingredients"]):
                payment = count_coins(coins, drink["cost"])
                if is_money_enough(payment, drink["cost"]):
                    make_coffee(resources, order, drink["ingredients"])
                    # order = MENU[order] -> the coffee type from the menu  (used to print the coffee type)
                    # drink["ingredients"] -> the 'ingredients' values of all coffee types (the function is adding the specific coffee type later on)


if __name__ == "__main__":
    main()
