# Number of rows
rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        # Check if row is even or odd
        if i % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()  # Move to next line