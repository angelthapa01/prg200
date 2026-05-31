# bs month names
bs_months = [
    "Baisakh", "Jestha", "Ashadh", "Shrawan",
    "Bhadra", "Ashwin", "Kartik", "Mangsir",
    "Poush", "Magh", "Falgun", "Chaitra"
]

# customer data
customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"}
]


def convert_date(date_str, from_cal, to_cal):

    # split date into parts
    year, month, day = map(int, date_str.split("-"))

    # convert year
    if from_cal == to_cal:
        converted_year = year

    elif from_cal == "AD" and to_cal == "BS":
        converted_year = year + 56

    elif from_cal == "BS" and to_cal == "AD":
        converted_year = year - 56

    else:
        return "Invalid conversion"

    return f"{converted_year:04d}-{month:02d}-{day:02d}"


for customer in customers:

    converted = convert_date(
        customer["date"],
        customer["cal"],
        customer["need"]
    )

    if customer["style"] == "full":
        year, month, day = map(int, converted.split("-"))
        month_name = bs_months[month - 1]
        converted = f"{day}th {month_name}, {year} {customer['need']}"

    print(
        f"{customer['name']} | Original: {customer['date']} {customer['cal']} | Converted: {converted}"
    )