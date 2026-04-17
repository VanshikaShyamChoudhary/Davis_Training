#Tail Implementation (Like Linux tail)
#Display last N lines of a file efficiently
n = int(input("Enter number of lines: "))

with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines[-n:]:
    print(line.strip())
