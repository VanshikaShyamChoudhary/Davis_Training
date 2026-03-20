 # Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# Loop to process marks of 5 students
for i in range(1, 6):
    marks = int(input(f"Enter marks for student {i}: "))
    grade = calculate_grade(marks)
    print(f"Student {i} Grade: {grade}")