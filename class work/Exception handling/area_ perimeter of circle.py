#WAP to find out the area and perimeter of circle while taking the input from the user
import math   # Import math module to use the value of pi

try:
    # Take radius input from the user
    radius = float(input("Enter the radius of the circle: "))
    
    # Check if the radius is negative
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    # Calculate area of the circle (pi * r^2)
    area = math.pi * radius * radius

    # Calculate perimeter (circumference) of the circle (2 * pi * r)
    perimeter = 2 * math.pi * radius

    # Display the results
    print("Area of circle =", area)
    print("Perimeter of circle =", perimeter)

# Handles invalid input like text or negative numbers
except ValueError as e:
    print("Invalid input:", e)

# Handles any other unexpected errors
except Exception as e:
    print("Something went wrong:", e)
