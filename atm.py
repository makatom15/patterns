class ATM:
    def __init__(self):
        self.display = None
        self.card_reader = None
        self.keypad = None
        self.cash_dispenser = None

class ATMBuilder:
    def __init__(self):
        self.atm = ATM()

    def add_display(self, display):
        self.atm.display = display

    def add_card_reader(self, card_reader):
        self.atm.card_reader = card_reader

    def add_keypad(self, keypad):
        self.atm.keypad = keypad

    def add_cash_dispenser(self, cash_dispenser):
        self.atm.cash_dispenser = cash_dispenser

    def get_atm(self):
        return self.atm