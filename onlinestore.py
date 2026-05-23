# Online Store Discount System

# taking input from user
purchase = float(input("Enter total purchase amount: "))
member = input("Are you a loyalty member? (yes/no): ")

# checking discount
if purchase < 1000:
    discount = 0

elif purchase >= 1000 and purchase <= 4999:
    discount = 5

elif purchase >= 5000 and purchase <= 14999:
    discount = 10

else:
    discount = 20

# applying discount
discount_amount = purchase * discount / 100
final_amount = purchase - discount_amount

# extra discount for loyalty members
if member == "yes":
    loyalty_discount = final_amount * 5 / 100
    final_amount = final_amount - loyalty_discount

# final output
print("Final payable amount: NPR", final_amount)