class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        if cents > 99:
            self.dollars += (cents // 100)
            self.cents = (cents % 100)
        else:
            self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        if deposit_cents + self.cents > 99:
            self.dollars += (deposit_cents + self.cents) // 100
            self.cents = (deposit_cents + self.cents) % 100
        else:
            self.cents += deposit_cents
