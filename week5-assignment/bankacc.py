class BankAccount:
    def __init__(self, name, account_number, balance=0):
        # store account details
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # add money to account
        self.balance += amount

    def withdraw(self, amount):
        # check if enough balance exists
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        # display current balance
        print(f"{self.name} ({self.account_number}) : NPR {self.balance}")


accounts = [
    ("Angel Thapa", "A001", 5000),
    ("Jessica Karki", "A002", 0),
    ("Agrata Rai", "A003", 12000)
]

bank_accounts = []

for name, acc_no, balance in accounts:
    bank_accounts.append(BankAccount(name, acc_no, balance))

# perform transactions
bank_accounts[1].deposit(3000)
bank_accounts[2].withdraw(15000)
bank_accounts[0].withdraw(2000)

print("Final Balances")
for account in bank_accounts:
    account.get_balance()