# Function for ATM withdrawal
def atm_system():
    balance = 10000
    
    while True:
        print(f"\nCurrent Balance: {balance}")
        amount = float(input("Enter withdrawal amount (or 0 to exit): "))
        
        if amount == 0:
            print("Thank you! Exiting ATM.")
            break
        
        # Conditions
        if amount < 0:
            print("Invalid amount! Please enter a positive value.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("Withdrawal Successful!")
            print(f"Remaining Balance: {balance}")

# Run ATM system
atm_system()