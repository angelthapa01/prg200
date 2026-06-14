import random

# this program splits a restaurant bill and selects one lucky person

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]

total_bill = 3750


def split_bill(friends, total):
    return total / len(friends)


def pick_lucky(friends):
    return random.choice(friends)


def final_summary(friends, total):
    share = split_bill(friends, total)
    lucky_person = pick_lucky(friends)

    print("bill summary")

    for friend in friends:
        print(friend, "pays npr", round(share, 2))

    # extra amount paid by the lucky person
    lucky_total = share + 50

    print("\nlucky person:", lucky_person)
    print("amount paid by lucky person:", round(lucky_total, 2))


final_summary(friends, total_bill)