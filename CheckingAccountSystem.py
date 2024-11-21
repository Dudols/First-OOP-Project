class CheckingAccount:

    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.balance = 0
        self.limit = None

    def check_balance(self):
        print(f'Your current balance is R${self.balance:.2f}')

    def add_balance(self, value_added):
        self.balance += value_added

    def _account_limit(self):
        self.limit = -1000
        return self.limit

    def check_limit(self):
        print(f'Your account limit is R${self.limit:.2f}')

    def withdraw_balance(self, value_withdrawal):
        if self.balance - value_withdrawal < self.account_limit():
            print(f'Operation not authorized. Balance is not avaiable')
            self.check_balance()
        else:
            self.balance -= value_withdrawal
            self.check_balance()

    def wire_money(self, value_wired, to_account):
        if self.balance - value_wired < self.account_limit():
            print(f'Operation not authorized. Balance is not avaiable')
            self.check_balance()
        else:
            self.balance -= value_wired
            to_account.balance += value_wired
            print(self.name), self.check_balance()
            print(to_account.name), to_account.check_balance()


conta_du = CheckingAccount('Eduardo', '123.456.789-00')
conta_ale = CheckingAccount('Alessandra', '098.765.432-11')

conta_du.add_balance(100000)
conta_du.wire_money(10000, conta_ale)