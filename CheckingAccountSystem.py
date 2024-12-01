from datetime import datetime
import pytz


class CheckingAccount:
    """
    Creates a Checking Account for a client.

    Attributes:
        name (str): Clients name
        cpf (str): Clients individual national social security number for brazilian residents. Must be inserted in the XXX.XXX.XXX-XX format.
        balance (float): Clients total balance in the account
        limit (float): Clients limit for transactions
        transactions (list): Clients complete transaction history
    """

    @staticmethod
    def _date_and_time():
        """
        Auxiliary static method to register time and date for transactions history

        Attributes:
            None
        """
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
        """
        Prints the account total balance.

        Attributes:
            None
        """
        print(f'Your current balance is R${self.balance:.2f}')

    def add_balance(self, value_added):
        """
        Adds balance for the clients account balance and registers the transaction in the transactions history.

        Attributes:
            value_added (float): value to be added to the account balance.
        """
        self.balance += value_added
        self.transactions.append((value_added, self.balance, CheckingAccount._date_and_time()))

    def _account_limit(self):
        """
        Defines the clients account limit for transactions.

        Attributes:
            None
        """
        self.limit = -1000
        return self.limit

    def check_limit(self):
        """
        Prints the account limit for transactions.

        Attributes:
            None
        """
        print(f'Your account limit is R${self.limit:.2f}')

    def withdraw_balance(self, value_withdrawl):
        """
        Removes balance from the clients account balance and registers the transaction in the transactions history.

        Attributes:
            value_withdrawl (float): value to be removed from the account balance.
        """
        if self.balance - value_withdrawl < self._account_limit():
            print(f'Operation not authorized. Balance is not avaiable')
            self.check_balance()
        else:
            self.balance -= value_withdrawl
            self.check_balance()
            self.transactions.append((-value_withdrawl, self.balance, CheckingAccount._date_and_time()))

    def wire_money(self, value_wired, to_account):
        """
        Removes balance from one clients account balance and adds it to another clients account.
        Also registers both transactions in the transactions history of the respective accounts.

        Attributes:
            value_wired (float): value to be removed from the first account balance and added to the other one.
            to_account (class instance): account to which the money must be transferred to.
        """
        if self.balance - value_wired < self._account_limit():
            print(f'Operation not authorized. Balance is not avaiable')
            self.check_balance()
        else:
            self.balance -= value_wired
            self.transactions.append((-value_wired, self.balance, CheckingAccount._date_and_time()))
            to_account.balance += value_wired
            to_account.transactions.append((value_wired, to_account.balance, CheckingAccount._date_and_time()))
            print(self.name), self.check_balance()
            print(to_account.name), to_account.check_balance()
        
    def check_transactions_history(self):
        """
        Prints the past transactions history in a python list of tuples.

        Attributes:
            None
        """
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