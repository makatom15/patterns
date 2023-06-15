from banknote import Banknote, BanknoteFactory
from coin import Coin, CoinFactory
from atm import ATMBuilder

# Создание объектов с использованием паттерна Фабрика
banknote_factory = BanknoteFactory()
banknote_10 = banknote_factory.create_banknote(10)
print("Значение банкноты:", banknote_10.value)

coin_factory = CoinFactory()
coin_1 = coin_factory.create_coin(1)
print("Значение монеты:", coin_1.value)

# Создание объектов с использованием паттерна Абстрактная фабрика
banknote_factory = BanknoteFactory()
banknote_50 = banknote_factory.create_banknote(50)
print("Значение банкноты:", banknote_50.value)

coin_factory = CoinFactory()
coin_5 = coin_factory.create_coin(5)
print("Значение монеты:", coin_5.value)

# Создание и настройка объекта банкомата с использованием паттерна Строитель
atm_builder = ATMBuilder()
atm_builder.add_display("LCD дисплей")
atm_builder.add_card_reader("Считыватель карт")
atm_builder.add_keypad("Сенсорная клавиатура")
atm_builder.add_cash_dispenser("Купюроприемник")

atm = atm_builder.get_atm()

print("Дисплей банкомата:", atm.display)
print("Считыватель карт банкомата:", atm.card_reader)
print("Клавиатура банкомата:", atm.keypad)
print("Купюроприемник банкомата:", atm.cash_dispenser)
