class CheckingAccount:

    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.balance = 0

    def add_balance(self, value_added):
        self.balance += value_added

    def wire_money(self, value_wired):
        self.balance -= value_wired

    def withdraw_balance(self, value_withdrawal):
        value = self.balance - value_withdrawal
        if value < 0:
            print(f'Operation not authorized. Balance is not avaiable')
        else:
            self.balance -= value_withdrawal

    def check_balance(self):
        print(f'Your current balance is R${self.balance:.2f}')

conta_du = CheckingAccount('Eduardo', '123.456.789-00')
