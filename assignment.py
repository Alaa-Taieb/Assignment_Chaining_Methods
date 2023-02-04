class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self
    
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f"User: Money Transfered from {self.name} to {other_user.name}")
        return self
    
elon_musk = User("Elon Musk", "elon@tesla.com")
jordan_peterson = User("Jordan Peterson" , "jordan@gmail.com")
alaa_taieb = User("Alaa Taieb", "alaataieb.tn@gmail.com")



elon_musk.make_deposit(15000000).make_deposit(300000000).make_deposit(1300000000).make_withdrawal(45000).display_user_balance()

jordan_peterson.make_deposit(200000).make_deposit(150000).make_withdrawal(25000).make_withdrawal(82500).display_user_balance()

alaa_taieb.make_deposit(333).make_withdrawal(3).make_withdrawal(5).make_withdrawal(7).display_user_balance()

elon_musk.transfer_money(alaa_taieb, 1000000000)




