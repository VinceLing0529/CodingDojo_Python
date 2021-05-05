class User:
    def __init__(self,name,balance):
        self.name=name
        self.balance = balance
    def make_deposit(self,amount):
        self.balance+=amount
        return self
    def make_withdraw(self,amount):
        self.balance-=amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")

        
a=User("Henry",500)
a.make_deposit(200).make_deposit(200).make_deposit(200).make_withdraw(100).display_user_balance()

b=User("Tom",300)
b.make_deposit(200).make_deposit(200).make_withdraw(100).make_withdraw(100).display_user_balance()

c=User("MARY",1000)
c.make_deposit(200).make_withdraw(100).make_withdraw(100).make_withdraw(100).display_user_balance()
