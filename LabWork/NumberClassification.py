# Function to classify number
def classify_number(num):
    # Check Positive / Negative / Zero
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"
    
    # Nested if for Even / Odd
    if num != 0:
        if num % 2 == 0:
            eo = "Even"
        else:
            eo = "Odd"
    else:
        eo = "Neither Even nor Odd"
    
    return sign, eo

# List of numbers
numbers = [10, -5, 0, 7, -8, 12]

# Loop to process all numbers
for num in numbers:
    sign, eo = classify_number(num)
    print(f"{num} → {sign}, {eo}")