from bank_account import BankAccount

class PremiumBankAccount(BankAccount):

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.__cashback_percent = 10

    def get_cashback_percent(self):
        return self.__cashback_percent

    def set_cashback_percent(self, percent):
        self.__cashback_percent = percent

    def transfer(self, other_bank_account, amount):
        super().transfer(other_bank_account, amount)
        self.set_balance(self.get_balance() + amount * self.__cashback_percent / 100)


premium1 = PremiumBankAccount('1111222233334444', 10 ** 6)
premium2 = PremiumBankAccount('1111222233334444', 10 ** 6)

# print(premium1.get_cashback_percent())
premium1.transfer(premium2, 10 ** 5)
print(premium1.get_balance())
print(premium2.get_balance())

print(PremiumBankAccount.__mro__)   # method resolution order
print(PremiumBankAccount.__dict__)