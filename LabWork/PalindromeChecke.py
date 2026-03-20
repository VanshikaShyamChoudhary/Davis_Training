# Function to check palindrome
def is_palindrome(value):
    value = str(value)  # convert to string
    rev = ""

    # Reverse using loop
    for ch in value:
        rev = ch + rev

    # Check palindrome
    if value == rev:
        print(f"{value} is a Palindrome")
    else:
        print(f"{value} is NOT a Palindrome")

# Take input
data = input("Enter a number or string: ")

# Call function
is_palindrome(data)