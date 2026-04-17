#WAP to copy the content of one file into another file
# Copy content from one file to another

with open("source.txt", "r") as source:
    with open("destination.txt", "w") as destination:
        content = source.read()
        destination.write(content)
        print("File copied successfully!")

