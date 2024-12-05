# Напишите класс BankAccount, который управляет балансом счета. Он должен
# поддерживать следующие методы:
# ● deposit(amount): добавляет указанную сумму к балансу.
# ● withdraw(amount): снимает указанную сумму с баланса, если достаточно
# средств.
# ● get_balance(): возвращает текущий баланс счета.
# При попытке снять больше средств, чем доступно на счете, должно
# выбрасываться исключение InsufficientFundsError. Напишите как минимум
# 5 тестов для проверки работы классов и его методов.
import pytest

@pytest.fixture
def bank_account():
    return BankAccount(100)

def test_show_balance(bank_account):
    assert bank_account.get_balance() == 'ваш текущий баланс - 100'

def test_deposit(bank_account):
    assert bank_account.deposit(50) == None

def test_withdraw(bank_account):
    assert bank_account.withdraw(50) == None

def test_none_withdraw(bank_account):
    assert bank_account.withdraw(150) == f'на вашем счёте недостаточно средств'


class InsufficientFundsError(Exception):
    def __str__(self):
        return f'на вашем счёте недостаточно средств'


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            raise InsufficientFundsError

    def get_balance(self):
        return f'ваш текущий баланс - {self.balance}'

if __name__ == '__main__':
    card = BankAccount(100)
    print(card.get_balance())
    card.deposit(200)
    print(card.get_balance())
    # card.withdraw(400)






