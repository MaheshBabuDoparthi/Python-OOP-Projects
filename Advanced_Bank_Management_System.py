# Project 12: Advanced Bank Management System
# Author: Mahesh Babu Doparthi

class Bank:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def show_details(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: ₹", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully!")
        print("Updated Balance: ₹", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance: ₹", self.balance)
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print("Current Balance: ₹", self.balance)

    def search_account(self, account_number):
        if self.account_number == account_number:
            print("Account Found!")
        else:
            print("Account Not Found!")


accounts = []

while True:

    print("\n========== Advanced Bank Management System ==========")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Search Account")
    print("7. Delete Account")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter Account Holder Name: ")
        account_number = int(input("Enter Account Number: "))
        balance = float(input("Enter Initial Balance: "))

        account = Bank(name, account_number, balance)
        accounts.append(account)

        print("Account Created Successfully!")

    elif choice == 2:

        if len(accounts) == 0:
            print("No Accounts Found!")
        else:
            for account in accounts:
                account.show_details()
                print("--------------------------")

    elif choice == 3:

        acc = int(input("Enter Account Number: "))

        for account in accounts:
            if account.account_number == acc:
                amount = float(input("Enter Deposit Amount: "))
                account.deposit(amount)
                break
        else:
            print("Account Not Found!")

    elif choice == 4:

        acc = int(input("Enter Account Number: "))

        for account in accounts:
            if account.account_number == acc:
                amount = float(input("Enter Withdrawal Amount: "))
                account.withdraw(amount)
                break
        else:
            print("Account Not Found!")

    elif choice == 5:

        acc = int(input("Enter Account Number: "))

        for account in accounts:
            if account.account_number == acc:
                account.check_balance()
                break
        else:
            print("Account Not Found!")

    elif choice == 6:

        acc = int(input("Enter Account Number: "))

        for account in accounts:
            if account.account_number == acc:
                account.search_account(acc)
                break
        else:
            print("Account Not Found!")

    elif choice == 7:

        acc = int(input("Enter Account Number: "))

        for account in accounts:
            if account.account_number == acc:
                accounts.remove(account)
                print("Account Deleted Successfully!")
                break
        else:
            print("Account Not Found!")

    elif choice == 8:
        print("Thank You for Using Advanced Bank Management System!")
        break

    else:
        print("Invalid Choice!")