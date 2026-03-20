# Login function
def login():
    correct_username = "admin"
    correct_password = "1234"
    
    attempts = 0
    
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username == correct_username and password == correct_password:
            print("Login Successful")
            return
        else:
            attempts += 1
            print("Invalid credentials")
    
    print("Account Locked")

# Call function
login()