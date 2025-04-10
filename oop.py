#Class Definition for BankAccount
# It has properties: Account Name and Balance Amount
# It has methods (actions): deposit() and withdraw()
class BankAccount:
    #__init__ function is called when an object is created
    def __init__(self, name, amount):
        # `self` is a variable that denotes the object itself
        # So, when we write self.account_name, account_name is a property of the object
        self.account_name = name
        self.balance = amount

    #Method/Action/Function to add some amount to the balance
    def deposit(self, amount):
        self.balance += amount
    
    #Method/Action/Function to subtract some amount to the balance
    def withdraw(self, amount):
        self.balance -= amount\
    
    def show_balance(self):
        print("The current balance is Rs. ", self.balance)


# Class Definition of SavingsAccount
# SavingsAccount is a CHILD class of BankAccount
# which means SavingsAccount INHERITS BankAccount class. This is called inheritance
class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05 #suppose interest rate is 5%
        self.balance += interest


#**********Class Definitions Finished**********#

#Implementation of Class by creating OBJECTS

account1 = SavingsAccount("John Doe", 500000)
account1.show_balance()

account1.deposit(2000)
account1.show_balance()

account1.withdraw(5999)
account1.show_balance()

account1.add_interest()
account1.show_balance()
