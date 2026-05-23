

passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special_characters = "!@#$%^&*"

# checking each password
for password in passwords:

    print("\nChecking password:", password)

    missing = []

    # checking length
    if len(password) < 8:
        missing.append("Minimum 8 characters")

    # checking uppercase letter
    if not any(char.isupper() for char in password):
        missing.append("Uppercase letter")

    # checking lowercase letter
    if not any(char.islower() for char in password):
        missing.append("Lowercase letter")

    # checking digit
    if not any(char.isdigit() for char in password):
        missing.append("Digit")

    # checking special character
    if not any(char in special_characters for char in password):
        missing.append("Special character")

    # final result
    if len(missing) == 0:
        print("Strong Password")

    else:
        print("Weak Password")
        print("Missing:", ", ".join(missing))