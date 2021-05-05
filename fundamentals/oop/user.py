class User:
    def __init__(self,name,balance):
        self.name=name
        self.balance = balance
        self.otherbanlance=200
        self.othername=""
    def make_deposit(self,amount):
        self.balance+=amount
    def make_withdraw(self,amount):
        self.balance-=amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
    def transfer_money(self, other_user, amount):
        self.othername=other_user
        self.balance-=amount
        self.otherbanlance+=amount
        
a=User("Henry",500)
a.make_deposit(200)
a.make_deposit(200)
a.make_deposit(200)
a.make_withdraw(100)
a.display_user_balance()

a=User("Tom",300)
a.make_deposit(200)
a.make_deposit(200)
a.make_withdraw(100)
a.make_withdraw(100)
a.display_user_balance()

a=User("MARY",1000)
a.make_deposit(200)
a.make_withdraw(100)
a.make_withdraw(100)
a.make_withdraw(100)
a.display_user_balance()