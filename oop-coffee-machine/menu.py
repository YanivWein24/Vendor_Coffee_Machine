from prettytable import PrettyTable


class MenuItem:  # coffee types
    """model for coffee types"""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24.0, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18.0, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0),
            MenuItem(name="americano", water=300, milk=0, coffee=26.0, cost=2.0),
        ]

    def print_items(self):
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
            [
                "Espresso\n\n\n",
                "Latte\n\n\n\n",
                "Cappuccino\n\n\n\n",
                "Americano\n\n\n",
            ],
        )
        table.add_column("Ingredients", all_coffee_ingredients)
        table.add_column("Cost", ["$ 1.5", "$ 2.5", "$ 3.0", "$ 2.0"])
        table.align = "l"
        print("\n")
        print(table)

    def find_drink(self, order_name):
        """Search if the ordered drink is available in the menu. if it does, return the drink. if not, return None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("\n* Sorry that item is not available. *")
