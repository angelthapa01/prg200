# inventory data
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

# customer cart
cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}


def process_order(inventory, cart):
    grand_total = 0

    print("---- bill ----")

    for item, quantity in cart.items():

        # check stock availability
        if inventory[item]["stock"] >= quantity:

            price = inventory[item]["price"]
            item_total = price * quantity

            # add to bill
            grand_total += item_total

            # update stock
            inventory[item]["stock"] -= quantity

            print(f"{item} x{quantity} = NPR {item_total}")

        else:
            print(f"Sorry, not enough stock for {item}")

    print(f"Grand Total: NPR {grand_total}")
    print("----------------")

    # display updated inventory
    print("Updated stock:")

    stock_list = []
    for item in inventory:
        stock_list.append(f"{item}={inventory[item]['stock']}")

    print(", ".join(stock_list))


process_order(inventory, cart)