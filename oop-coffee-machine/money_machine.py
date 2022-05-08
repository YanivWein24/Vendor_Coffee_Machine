class MoneyMachine:

    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"\n* Total amount of money: {self.profit}")

    def process_coins(self, cost):
        """Returns the total calculated from coins inserted."""
        print(f"\nThis drink cost: ${cost}")
        print("\nPlease insert coins: \n")
        for coin in self.COIN_VALUES:
            self.money_received += (
                int(input(f"how many {coin}? ")) * self.COIN_VALUES[coin]
            )
        print(f"\nYou inserted: ${round(self.money_received, 2)}")
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins(cost)  # adding money to self.money_received
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if self.money_received > cost:
                print(f"This is your change: ${change}")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
