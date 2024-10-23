class BankAccount:
    def __init__(self, account_number, balance):
        self.set_account_number(account_number)
        self.set_balance(balance)

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        if len(account_number) == 16 and account_number.isdigit():
            self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance

    def transfer(self, other_bank_account, amount):
        if isinstance(other_bank_account, BankAccount):
            if 0 < amount < self.get_balance():
                self.set_balance(self.get_balance() - amount)
                # self.__balance -= amount
                other_bank_account.set_balance(other_bank_account.get_balance() + amount)
            else:
                print('Not enough funds...')
        else:
            print('Unknown account...')


if __name__ == '__main__':
    account1 = BankAccount('1111222233334444 ', 10 ** 6)
    account2 = BankAccount('2222111133334444 ', 10 ** 4)

    print(account1.get_balance())
    account1.transfer(account2, 10 ** 3)
    print(account1.get_balance())
    print(account2.get_balance())