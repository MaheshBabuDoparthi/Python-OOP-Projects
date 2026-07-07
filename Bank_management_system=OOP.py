class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance!")

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount("Mahesh", 5000)

account.deposit(1000)
account.withdraw(2000)
account.show_balance()