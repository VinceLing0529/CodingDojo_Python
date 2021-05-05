class User:
    def __init__(self):
        self.name="tom"
        self.balance = 300
        self.otherbanlance=200
        self.othername=""
    def make_withdraw(self,amount):
        self.balance-=amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
    def transfer_money(self, other_user, amount):
        self.othername=other_user
        self.balance-=amount
        self.otherbanlance+=amount
        
x=User()
x.make_withdraw(100)
x.display_user_balance()
x.transfer_money("mary",200)
print(x.otherbanlance)
print(x.balance)