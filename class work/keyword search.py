#Ask user for a keyword and return all lines from file containing that keyword
# Take keyword from user
keyword = input("Enter keyword to search: ")

# Open file
with open("input.txt", "r") as file:
    found = False
    
    for line in file:
        if keyword in line:
            print(line.strip())
            found = True

    if not found:
        print("Keyword not found!")
