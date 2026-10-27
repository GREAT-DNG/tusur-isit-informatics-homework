class Account:
    def __init__(self, number: str, owner: str, balance: int = 0):
        if balance < 0: raise ValueError
        self.number = number
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"

    def deposit(self, amount: int): 
        if amount <= 0: raise ValueError
        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance < amount or amount <= 0: raise ValueError
        self.balance -= amount
