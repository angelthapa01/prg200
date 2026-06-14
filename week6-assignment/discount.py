# this module handles discounts and tax calculations

TAX_RATE = 0.13


def apply_discount(price, percent):
    return price - (price * percent / 100)


def apply_tax(price):
    return price + (price * TAX_RATE)


def final_price(price, discount_pct):
    discounted_price = apply_discount(price, discount_pct)

    # apply tax after discount
    return apply_tax(discounted_price)