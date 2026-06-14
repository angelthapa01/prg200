from discount import final_price, TAX_RATE

# this program calculates final prices for products

products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0),
]

print("tax rate:", TAX_RATE)

for name, price, discount in products:
    final = final_price(price, discount)

    print("\nproduct:", name)
    print("original price:", price)
    print("final price:", round(final, 2))