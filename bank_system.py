class Account:
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
    def __init__(self, number: str, owner: str, balance: int = 0, rate: float = 0.05):
        super().__init__(number, owner, balance)
        self.rate = rate

    def __repr__(self):
        return f"SavingsAccount('{self.number}', '{self.owner}', {self._balance}, {self.rate})"

    def add_interest(self):
        self._balance += self._balance * self.rate

class CheckingAccount(Account):
    def __init__(self, number: str, owner: str, balance: int = 0, overdraft: int = 0):
        super().__init__(number, owner, balance)
        self.overdraft = overdraft

    def __repr__(self):
        return f"CheckingAccount('{self.number}', '{self.owner}', {self._balance}, {self.overdraft})"

    def withdraw(self, amount: int):
        if self._balance + self.overdraft < amount or amount <= 0: raise ValueError
        self._balance -= amount

class Customer():
    def __init__(self, name: str, customer_id: str):
        self.name = name
        self.customer_id = customer_id
        self._accounts = []

    def accounts(self):
        return self._accounts

    def add_account(self, account: Account):
        self._accounts.append(account)

    def remove_account(self, number: str):
        for i in range(len(self._accounts)):
            if self._accounts[i].number == number:
                del self._accounts[i]
                return

    def total_balance(self):
        result = 0
        for i in self._accounts:
            result += i.balance
        return result

class Bank():
    def __init__(self):
        self.customers = []

    def add_customer(self, customer: Customer):
        for i in self.customers:
            if customer.customer_id == i.customer_id: raise ValueError
        self.customers.append(customer)

    def customer(self, customer_id: str):
        for i in self.customers:
            if i.customer_id == customer_id: return i
        raise KeyError

    def account(self, number: str, raise_error: bool = True):
        for i in self.customers:
            for j in i.accounts():
                if j.number == number: return {"customer": i, "account": j}
        if raise_error: raise KeyError

    def open_account(self, customer_id: str, account: Account):
        if self.account(account.number, False) != None: raise ValueError
        self.customer(customer_id).add_account(account)

    def close_account(self, number: str):
        account_data = self.account(number)
        if account_data["account"].balance != 0: raise ValueError # pyright: ignore
        account_data["customer"].remove_account(number) # pyright: ignore
        
    def transfer(self, from_number: str, to_number: str, amount: int):
        if from_number == to_number: raise ValueError
        from_account_data = self.account(from_number)
        to_account_data = self.account(to_number)
        from_account_data["account"].withdraw(amount) # pyright: ignore
        to_account_data["account"].deposit(amount) # pyright: ignore

    def accounts(self, customer_id: str, min_balance: int | None = None):
        customer = self.customer(customer_id)
        if min_balance == None:
            return customer.accounts()
        else:
            result = []
            for i in customer.accounts():
                if i.balance > min_balance: result.append(i)
            return result

    def total_deposits(self):
        result = 0
        for i in self.customers:
            for j in i.accounts():
                result += j.balance
        return result
