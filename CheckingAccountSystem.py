from datetime import datetime
import pytz


class CheckingAccount:

    @staticmethod
    def _date_and_time():
            timezone_BR = pytz.timezone('America/Sao_Paulo')
            time_BR = datetime.now(timezone_BR)
            return time_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.balance = 0
        self.limit = None
        self.transactions = []

    def check_balance(self):
        print(f'Your current balance is R${self.balance:.2f}')

    def add_balance(self, value_added):
        self.balance += value_added
        self.transactions.append((value_added, self.balance, CheckingAccount._date_and_time()))

    def _account_limit(self):
        self.limit = -1000
        return self.limit

    def check_limit(self):
        print(f'Your account limit is R${self.limit:.2f}')

    def withdraw_balance(self, value_withdrawal):
        if self.balance - value_withdrawal < self._account_limit():
            print(f'Operation not authorized. Balance is not avaiable')
            self.check_balance()
        else:
            self.balance -= value_withdrawal
            self.check_balance()
            self.transactions.append((-value_withdrawal, self.balance, CheckingAccount._date_and_time()))

    def wire_money(self, value_wired, to_account):
        if self.balance - value_wired < self._account_limit():
            print(f'Operation not authorized. Balance is not avaiable')
            self.check_balance()
        else:
            self.balance -= value_wired
            to_account.balance += value_wired
            print(self.name), self.check_balance()
            print(to_account.name), to_account.check_balance()
        
    def check_transactions_history(self):
        print('Past Transactions')
        for transaction in self.transactions:
            print(transaction)


account_du = CheckingAccount('Eduardo', '123.456.789-00')
account_ale = CheckingAccount('Alessandra', '098.765.432-11')
account_du.add_balance(100000)
print(account_du.transactions)
print('-' * 20)
account_du.wire_money(10000, account_ale)
print('-' * 20)
account_du.check_transactions_history()