class BankAccount:
    def __init__(self, int_rate=0, balance=0): 
        self.intrate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            self.balance-=5
            print("Insufficient funds: Charging a $5 fee")
        return self
    def display_account_info(self):
        print(f"Balance : {self.balance}")
        return self
    def yield_interest(self):
        self.total = self.intrate/100*self.balance
        print(self.total)
        return self
    @classmethod
    def allinfor(cls,balance,yi):
        print(f"Balance : {balance}, yield interest: {yi}")


class User:
    def __init__(self,name,balance):
        self.name=name
        self.account=BankAccount(balance=balance)
    def make_deposit(self,amount):
        self.account.deposit(amount)
    def make_withdraw(self,amount):
        self.account.deposit(amount)
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")


a=User("Henry",500)
a.make_deposit(300)
a.display_user_balance()