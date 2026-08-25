# Student Result Management System

students = {}
subjects = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    subject = input(f"Enter subject {i + 1}: ")
    subjects.append(subject)

while True:
    print("\n===== STUDENT RESULT MANAGEMENT =====")
    print("1. Add Student Marks")
    print("2. Display Results")
    print("3. Class Average")
    print("4. Topper")
    print("5. Subject-wise Highest Marks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")

        marks = {}

        for subject in subjects:
            while True:
                value = input(f"Enter marks in {subject} (0-100): ")

                # Missing subject entry
                if value == "":
                    print(f"Marks missing for {subject}. Taking 0.")
                    marks[subject] = 0
                    break

                try:
                    mark = float(value)

                    # Invalid marks
                    if mark < 0 or mark > 100:
                        print("Invalid marks! Enter marks between 0 and 100.")
                    else:
                        marks[subject] = mark
                        break

                except ValueError:
                    print("Invalid input! Please enter a number.")

        students[name] = marks
        print("Student added successfully!")

    # Display results
    elif choice == "2":

        if not students:
            print("No student records available.")
            continue

        print("\n========== STUDENT RESULTS ==========")

        for name, marks in students.items():

            total = sum(marks.values())
            percentage = total / len(subjects)

            # Grade
            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            # Pass/Fail
            status = "PASS" if all(mark >= 33 for mark in marks.values()) else "FAIL"

            print("\nStudent:", name)

            for subject, mark in marks.items():
                print(f"{subject}: {mark}")

            print("Total:", total)
            print(f"Percentage: {percentage:.2f}%")
            print("Grade:", grade)
            print("Status:", status)

    # Class average
    elif choice == "3":

        if not students:
            print("No student records available.")
            continue

        total_percentage = 0

        for marks in students.values():
            total = sum(marks.values())
            percentage = total / len(subjects)
            total_percentage += percentage

        average = total_percentage / len(students)

        print(f"\nClass Average: {average:.2f}%")

    # Topper
    elif choice == "4":

        if not students:
            print("No student records available.")
            continue

        topper = None
        highest_percentage = -1

        for name, marks in students.items():
            total = sum(marks.values())
            percentage = total / len(subjects)

            if percentage > highest_percentage:
                highest_percentage = percentage
                topper = name

        print("\n===== TOPPER =====")
        print("Name:", topper)
        print(f"Percentage: {highest_percentage:.2f}%")

    # Subject-wise highest marks
    elif choice == "5":

        if not students:
            print("No student records available.")
            continue

        print("\n===== SUBJECT-WISE HIGHEST MARKS =====")

        for subject in subjects:

            highest = -1
            highest_student = ""

            for name, marks in students.items():

                if marks[subject] > highest:
                    highest = marks[subject]
                    highest_student = name

            print(
                f"{subject}: {highest} marks "
                f"({highest_student})"
            )

    # Exit
    elif choice == "6":
        print("Thank you! Program ended.")
        break

    else:
        print("Invalid choice! Please try again.")