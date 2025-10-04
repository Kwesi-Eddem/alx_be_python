"""class BankAccount():
    
    def __init__(self, account_balance=0):
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
        print(f"Current Balance: ${self.account_balance:.1f}")"""

class BankAccount():  
    
    def __init__(self, account_balance): 
        self.account_balance = account_balance 
        account_balance = 0 
    
    def deposit(self, amount): 
        if amount > 0: 
            self.account_balance += amount 
        else: print('Amount must be greater than 0.') 
        
    def withdraw(self, amount): 
        if amount <= self.account_balance: 
            self.account_balance -= amount 
            return True 
        else: 
            return False 
    
    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")