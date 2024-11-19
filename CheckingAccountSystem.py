class CheckingAccount:

    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.balance = 0

    def add_balance(self, value_added):
        pass

    def wire_money(self, value_wired):
        pass

    def withdraw_balance(self, value_withdrawal):
        pass

conta_du = CheckingAccount('Eduardo', '123.456.789-00')