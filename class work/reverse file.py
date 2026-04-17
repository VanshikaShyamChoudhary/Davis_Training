'''Read a file and write its content in reverse order (line-wise) into another file '''
with open("input.txt", "r") as f:
    lines = f.readlines()

# Reverse the list of lines
lines.reverse()

with open("output.txt", "w") as f:
    f.writelines(lines)

print("File content reversed successfully!")
