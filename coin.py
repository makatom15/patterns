class Coin:
    def __init__(self, value):
        self.value = value

class CoinFactory:
    @staticmethod
    def create_coin(value):
        return Coin(value)