# Password Strength & Account Security

import time

# ---------- Password Strength Checker ----------

def check_password(password):

    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{};:,.?/"

    for char in password:

        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in special_characters:
            has_special = True

    score = 0
    suggestions = []

    # Length
    if length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase
    if has_upper:
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase
    if has_lower:
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Digit
    if has_digit:
        score += 1
    else:
        suggestions.append("Add at least one digit.")

    # Special character
    if has_special:
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


# ---------- Create Account ----------

print("========== CREATE ACCOUNT ==========")

username = input("Enter username: ")
password = input("Create password: ")

strength, suggestions = check_password(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("Password meets all requirements!")

# ---------- Login System ----------

MAX_ATTEMPTS = 3
LOCK_TIME = 10

failed_attempts = 0
locked_until = 0

print("\n========== LOGIN ==========")

while True:

    # Check account lock
    current_time = time.time()

    if current_time < locked_until:
        remaining = int(locked_until - current_time) + 1

        print(
            f"Account is temporarily locked. "
            f"Try again after {remaining} seconds."
        )

        time.sleep(2)
        continue

    login_username = input("\nEnter username: ")
    login_password = input("Enter password: ")

    # Correct login
    if login_username == username and login_password == password:

        print("\nLogin successful!")
        print("Welcome,", username)
        break

    # Wrong login
    else:

        failed_attempts += 1

        print("Invalid username or password.")

        remaining_attempts = MAX_ATTEMPTS - failed_attempts

        if failed_attempts >= MAX_ATTEMPTS:

            print("\nToo many failed attempts!")
            print(f"Account locked for {LOCK_TIME} seconds.")

            locked_until = time.time() + LOCK_TIME
            failed_attempts = 0

        else:

            print(
                f"Attempts remaining: "
                f"{remaining_attempts}"
            )