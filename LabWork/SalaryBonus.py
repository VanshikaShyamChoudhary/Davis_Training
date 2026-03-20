# Function to calculate bonus
def calculate_bonus(salary, experience):
    if experience >= 10:
        bonus = 0.20 * salary
    elif experience >= 5:
        bonus = 0.10 * salary
    else:
        bonus = 0.05 * salary
    
    return bonus

# Loop for multiple employees
n = int(input("Enter number of employees: "))

for i in range(1, n + 1):
    print(f"\nEmployee {i}:")
    salary = float(input("Enter salary: "))
    experience = int(input("Enter years of experience: "))
    
    bonus = calculate_bonus(salary, experience)
    total_salary = salary + bonus
    
    print(f"Bonus: {bonus}")
    print(f"Total Salary after bonus: {total_salary}")