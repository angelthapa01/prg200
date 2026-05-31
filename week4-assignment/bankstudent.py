accounts = {}


def create_account():
    name = input("Enter name: ")
    balance = float(input("Enter initial deposit: "))
    accounts[name] = balance
    print("Account created successfully")


def deposit():
    name = input("Enter name: ")
    amount = float(input("Enter amount to deposit: "))

    if name in accounts:
        accounts[name] += amount
        print("Money deposited")
    else:
        print("Account not found")


def withdraw():
    name = input("Enter name: ")
    amount = float(input("Enter amount to withdraw: "))

    if name in accounts:
        if accounts[name] - amount >= 100:
            accounts[name] -= amount
            print("Money withdrawn")
        else:
            print("Minimum balance should be 100")
    else:
        print("Account not found")


def check_balance():
    name = input("Enter name: ")

    if name in accounts:
        print("Balance =", accounts[name])
    else:
        print("Account not found")


def transfer():
    sender = input("Sender name: ")
    receiver = input("Receiver name: ")
    amount = float(input("Enter amount: "))

    if sender in accounts and receiver in accounts:
        if accounts[sender] >= amount:
            accounts[sender] -= amount
            accounts[receiver] += amount
            print("Transfer successful")
        else:
            print("Not enough balance")
    else:
        print("Account not found")


def show_accounts():
    print("\nAccount Holders:")
    
    for name in accounts:
        print(name)


while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. View All Accounts")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        check_balance()

    elif choice == "5":
        transfer()

    elif choice == "6":
        show_accounts()

    elif choice == "7":
        print("Thank you")
        break

    else:
        print("Invalid choice")