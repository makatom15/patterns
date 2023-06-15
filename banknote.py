class Banknote:
    def __init__(self, value):
        self.value = value

class BanknoteFactory:
    @staticmethod
    def create_banknote(value):
        return Banknote(value)