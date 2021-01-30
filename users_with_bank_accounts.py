class BankAccount:
    def __init__(self, rate=.01, balance=0):
        self.int_rate = rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        amount_after_withdraw = self.balance - amount
        if amount_after_withdraw < 0:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            interest_yielded = self.balance * self.int_rate
            self.balance += interest_yielded
        return self

class User:
    def __init__(self, name, email, int_rate=.01, balance=0):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate, balance)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Email: {self.email}")
        self.account.display_account_info()
        return self



jason = User('Jason', 'jason@python.com')
agnes = User('Agnes', 'agnes@python.com')

jason.make_deposit(10).make_deposit(10).make_deposit(10).make_withdrawl(5).display_user_balance()
agnes.make_deposit(20).make_deposit(20).make_withdrawl(5).make_withdrawl(5).make_withdrawl(5).make_withdrawl(5)

agnes.display_user_balance()
agnes.account.yield_interest()
agnes.display_user_balance()