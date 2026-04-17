#A file students.txt contains records in format:
#Name,Marks,City
#Extract and save only students scoring above 75 into a new file
# Open the source file in read mode
with open("student.txt", "r") as source:
    
    # Open the new file in write mode
    with open("output.txt", "w") as dest:
        
        # Read file line by line
        for line in source:
            data = line.strip().split(",")   # Split data
            
            name = data[0]
            marks = int(data[1])
            sign = data[2]
            
            # Check condition
            if marks > 75:
                dest.write(line)

print("Students with marks > 75 are saved successfully.")
