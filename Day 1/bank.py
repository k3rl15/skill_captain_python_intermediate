# This is a Python class for a BankAccount.
class BankAccount:
    # Constructor for the BankAccount class that initializes attributes.
    def __int__(self, account_number, account_holder_name, account_balance):
        self.account_number = account_number  # Account number of the bank account.
        self.account_holder_name = account_holder_name  # Name of the account holder.
        self.account_balance = account_balance  # Current balance of the account.

    # Method to deposit money into the account.
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount} into the account. New balance {self.account_balance}.")
        else:
            print("Invalid amount. Please deposit a positve amount.")

    # Method to withdraw money from the account.
    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew {amount} from the account. New balance {self.account_balance}.")
        elif amount < 0:
            print("Invalid amount. Please witdraw a positve amount.")
        else:
            print(f"Insufficent funds, withdrawal denied.")

    # Method to display account information.
    def display_acc_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Balance: {self.account_balance}")
