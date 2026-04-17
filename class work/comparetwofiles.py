# Find lines that are present in file1 but not in file2
# Read file2 and store its lines in a set
with open("file2.txt", "r") as f2:
    lines2 = set(f2.readlines())

# Compare with file1
with open("file1.txt", "r") as f1:
    for line in f1:
        if line not in lines2:
            print(line.strip())
