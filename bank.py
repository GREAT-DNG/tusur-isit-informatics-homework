class Account:
    number: str = ""
    owner: str = ""
    _balance: int | float = 0

    def __init__(self, number: str, owner: str, balance: int = 0):
        if balance < 0: raise ValueError
        self.number = number
        self.owner = owner
        self._balance = balance

    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self._balance})"

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: int): 
        if amount < 0: raise ValueError
        self._balance += amount

    def withdraw(self, amount: int):
        if self._balance < amount or amount <= 0: raise ValueError
        self._balance -= amount

class SavingsAccount(Account):
    rate: float = 0.0

    def __init__(self, number: str, owner: str, balance: int = 0, rate: float = 0.05):
        super().__init__(number, owner, balance)
        self.rate = rate

    def __repr__(self):
        return f"SavingsAccount('{self.number}', '{self.owner}', {self._balance}, {self.rate})"

    def add_interest(self):
        self._balance += self._balance * self.rate

class CheckingAccount(Account):
    overdraft: int = 0

    def __init__(self, number: str, owner: str, balance: int = 0, overdraft: int = 0):
        super().__init__(number, owner, balance)
        self.overdraft = overdraft

    def __repr__(self):
        return f"CheckingAccount('{self.number}', '{self.owner}', {self._balance}, {self.overdraft})"

    def withdraw(self, amount: int):
        if self._balance + self.overdraft < amount or amount <= 0: raise ValueError
        self._balance -= amount
