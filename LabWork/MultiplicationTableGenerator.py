# Function to generate multiplication table
def print_table(num):
    if num < 0:
        print("Negative numbers are not allowed")
    else:
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

# Take input from user
number = int(input("Enter a number: "))

# Call function
print_table(number)