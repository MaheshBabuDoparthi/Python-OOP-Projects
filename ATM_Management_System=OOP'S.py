# Project 4: ATM Management System (OOP)
# Author: Mahesh Babu Doparthi

class ATM:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def show_details(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully!")
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful!")
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Funds!")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Creating Object

atm1 = ATM("Mahesh", 123456789, 5000)

print("========== ATM DETAILS ==========")
atm1.show_details()

print("\n========== DEPOSIT ==========")
atm1.deposit(2000)

print("\n========== WITHDRAW ==========")
atm1.withdraw(1500)

print("\n========== BALANCE ==========")
atm1.check_balance()