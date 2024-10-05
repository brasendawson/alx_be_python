class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance, default to zero if not provided
        self.__account_balance = initial_balance

    def deposit(self, amount):
        # Adds the deposit amount to the account balance
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        # Deducts the amount from the account balance if sufficient funds exist
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        # Displays the current account balance in a user-friendly format
        print(f"Current Balance: ${self.__account_balance:.2f}")
