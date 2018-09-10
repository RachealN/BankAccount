class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = True

    def open(self):
        pass

    def get_balance(self):
        if self.status == False:
            raise ValueError('oops')
        return self.balance

    def deposit(self, amount):
        if self.status == False:
            raise ValueError('oops')
        if amount < 0:
            raise ValueError('Invalid Entry')

        self.balance += amount

    def withdraw(self, amount):
        if self.status == False:
            raise ValueError('oops')

        if amount > self.balance:
            raise ValueError('insuficient balance')

        if amount < 0:
            raise ValueError('Invalid Entry')

        self.balance -= amount

    def close(self):
        self.status=False
