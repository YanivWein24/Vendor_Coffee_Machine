from prettytable import PrettyTable


class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "water": 600,
            "milk": 250,
            "coffee": 100,
        }

    def report(self):
        """Prints a table containing the Machine's stock and total cash"""
        report_table = PrettyTable()
        report_table.add_column("Resource", ["Water", "Milk", "Coffee"])
        report_table.add_column(
            "Amount",
            [
                f"{self.resources['water']}ml\n",
                f"{self.resources['milk']}ml\n",
                f"{self.resources['coffee']}gr\n",
            ],
        )
        print("\n")
        print(report_table)

    def is_resource_sufficient(self, drink):  # drink's name
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        """Deducts the required ingredients from the resources."""
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕️. Enjoy!\n")

    def refill(self, password):
        """Receives the Machine's resources. Returns a full stock if stock is not full"""
        full_resources = {
            "water": 600,
            "milk": 250,
            "coffee": 100,
        }
        if self.resources == full_resources:
            print("\n* Stock already full *")
            return self.resources
        else:
            while True:
                confirmation = input(
                    "\nTo continue, please enter the administrator password: "
                ).lower()
                if confirmation == password:
                    print("\n* Stock refilled! *")
                    return full_resources
                    # break
                elif confirmation == "q":
                    print("\n* Process Canceled *")
                    return self.resources
                    break
                else:
                    print("\nPlease enter the correct password, or type 'q' to cancel")
