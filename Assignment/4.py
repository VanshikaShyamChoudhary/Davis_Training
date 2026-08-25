# Weather Data Analyzer

temperatures = []
rainfall = []

n = int(input("Enter number of days: "))

# Input weather data
for i in range(n):
    print(f"\nDay {i + 1}")

    temp = float(input("Enter temperature (°C): "))
    rain = float(input("Enter rainfall (mm): "))

    temperatures.append(temp)
    rainfall.append(rain)

# Basic calculations
average = sum(temperatures) / n
minimum = min(temperatures)
maximum = max(temperatures)

temperature_range = maximum - minimum

# Number of rainy days
rainy_days = 0

for rain in rainfall:
    if rain > 0:
        rainy_days += 1

# Hottest day
hottest_temperature = max(temperatures)
hottest_day = temperatures.index(hottest_temperature) + 1

# Display results
print("\n========== WEATHER ANALYSIS ==========")

print(f"Average Temperature : {average:.2f} °C")
print(f"Minimum Temperature : {minimum:.2f} °C")
print(f"Maximum Temperature : {maximum:.2f} °C")
print(f"Temperature Range   : {temperature_range:.2f} °C")
print(f"Number of Rainy Days: {rainy_days}")
print(
    f"Hottest Day         : Day {hottest_day} "
    f"({hottest_temperature:.2f} °C)"
)

# Threshold
threshold = float(
    input("\nEnter temperature threshold (°C): ")
)

print(
    f"\nDays where temperature crossed "
    f"{threshold} °C:"
)

crossed_days = []

for i in range(n):
    if temperatures[i] > threshold:
        crossed_days.append(i + 1)

if crossed_days:
    print(crossed_days)
else:
    print("No day crossed the threshold.")


# Consecutive days above threshold
print("\n===== CONSECUTIVE HOT DAYS =====")

start = None

for i in range(n):
    if temperatures[i] > threshold:

        if start is None:
            start = i

    else:

        if start is not None:
            end = i - 1

            if end - start + 1 >= 2:
                print(
                    f"Day {start + 1} to Day {end + 1}"
                )

            start = None

# Check if sequence continues till last day
if start is not None:
    end = n - 1

    if end - start + 1 >= 2:
        print(
            f"Day {start + 1} to Day {end + 1}"
        )