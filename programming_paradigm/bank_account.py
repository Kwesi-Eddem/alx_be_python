class BankAccount():
    
    def __init__(self, account_balance=0):
        print("BankAccount:")
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")
        
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print("BankAccount:")
        print(f"Current Balance: ${self.account_balance:.1f}")