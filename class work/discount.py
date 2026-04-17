#Question 1: A shopkeeper wants to calculate total bill after discount.
#Input: Enter price and discount percentage
#Output: Final price after discount
#Answer:-
#METHOD 1

# Taking input from user
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter discount percentage: "))

# Calculating discount amount
discount_amount = (price * discount_percent) / 100

# Calculating final price
final_price = price - discount_amount
# Display result
print("final price after discount is :" , final_price)

#METHOD 2

# Using direct formula in one line
price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))

final_price = price * (1 - discount / 100)

print("Final price after discount is:", final_price)

#METHOD 3

# Adding validation (different approach)

price = float(input("Enter original price: "))

while True:
    discount = float(input("Enter discount percentage: "))
    if 0 <= discount <= 100:
        break
    else:
        print("Enter valid discount (0-100)")

final_price = price - (price * discount / 100)

print("Final price after discount is:", final_price)

#METHOD 4

# Retry input until valid

while True:
    price = float(input("Enter price: "))
    discount = float(input("Enter discount percentage: "))

    if price > 0 and 0 <= discount <= 100:
        break
    print("Invalid input, try again.")

final_price = price - (price * discount / 100)

print("Final price:", final_price)

#METHOD 5

# Using map for input

price, discount = map(float, input("Enter price and discount: ").split())

final_price = price * (1 - discount / 100)

print("Final price:", final_price)
     

#METHOD 6

 price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

final_price = price - (price * discount / 100)

print("Final price:", round(final_price, 2))
     

 #METHOD 7

 # Discount + GST

price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

discounted_price = price - (price * discount / 100)

gst = discounted_price * 0.18  # 18% GST
final_price = discounted_price + gst

print("Final price after discount + GST:", final_price)

#METHOD 8

price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

if price > 1000:
    discount += 5  # extra 5% discount

final_price = price * (1 - discount / 100)

print("Final price:", final_price)




