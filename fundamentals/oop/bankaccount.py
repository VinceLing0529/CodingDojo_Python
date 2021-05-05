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

x=BankAccount(2)

x.deposit(200).deposit(200).deposit(200).withdraw(300).yield_interest().display_account_info()

y=BankAccount(3,500)

y.deposit(200).deposit(200).withdraw(100).withdraw(100).withdraw(300).withdraw(300).yield_interest().display_account_info()

y=BankAccount.allinfor(200,3)