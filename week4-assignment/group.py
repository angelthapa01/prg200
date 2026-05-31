def get_members():
    n = int(input("Number of members: "))
    return [input(f"Member {i+1}: ") for i in range(n)]


def get_expenses(members):
    return {m: float(input(f"Amount paid by {m}: ")) for m in members}


def show_result(expenses):
    total = sum(expenses.values())
    share = total / len(expenses)

    print("\n--- Expense Summary ---")
    print("Total Expense:", total)
    print("Share Per Person:", round(share, 2))

    for member, paid in expenses.items():
        balance = paid - share

        if balance > 0:
            print(f"{member} paid extra {balance:.2f}")
        elif balance < 0:
            print(f"{member} needs to pay {abs(balance):.2f}")
        else:
            print(f"{member} paid exact amount")


def main():
    members = get_members()
    expenses = get_expenses(members)
    show_result(expenses)


main()