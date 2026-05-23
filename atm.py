# ATM withdrawal program

# taking input from user
balance = int(input("Enter your balance: "))
daily_withdrawn = int(input("Enter amount already withdrawn today: "))
amount = int(input("Enter amount to withdraw: "))

# checking if amount is multiple of 500
if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")

# checking balance
elif amount > balance:
    print("Insufficient balance.")

# checking daily withdrawal limit
elif daily_withdrawn + amount > 50000:
    print("Daily withdrawal limit reached.")

# withdrawal successful
else:
    balance = balance - amount
    print("Withdrawal successful.")
    print("Your current balance after withdrawal: NPR", balance)