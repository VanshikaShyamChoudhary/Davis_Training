# Problem Statement
# 
## E-Commerce Shopping Cart

cart = {}

while True:
    print("\n------ E-COMMERCE SHOPPING CART ------")
    print("1. Add Product")
    print("2. Change Quantity")
    print("3. Remove Product")
    print("4. View Cart")
    print("5. Generate Invoice")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        if name in cart:
            cart[name]["quantity"] += quantity
        else:
            cart[name] = {
                "price": price,
                "quantity": quantity
            }

        print("Product added successfully!")

    elif choice == 2:
        name = input("Enter product name: ")

        if name in cart:
            quantity = int(input("Enter new quantity: "))

            if quantity > 0:
                cart[name]["quantity"] = quantity
                print("Quantity updated!")
            else:
                del cart[name]
                print("Product removed!")
        else:
            print("Product not found!")

    elif choice == 3:
        name = input("Enter product name: ")

        if name in cart:
            del cart[name]
            print("Product removed successfully!")
        else:
            print("Product not found!")

    elif choice == 4:
        if not cart:
            print("Cart is empty!")
        else:
            print("\n----- CART -----")
            for name, details in cart.items():
                total = details["price"] * details["quantity"]
                print(f"{name} | Price: ₹{details['price']:.2f} | "
                      f"Qty: {details['quantity']} | Total: ₹{total:.2f}")

    elif choice == 5:
        if not cart:
            print("Cart is empty!")
            continue

        subtotal = 0

        print("\n---------------------------------------")
        print("           E-COMMERCE INVOICE")
        print("--------------------------------------------")
        print(f"{'Product':15} {'Price':>8} {'Qty':>5} {'Total':>10}")
        print("----------------------------------------")

        expensive_item = None
        max_price = 0

        for name, details in cart.items():
            price = details["price"]
            quantity = details["quantity"]
            total = price * quantity

            subtotal += total

            print(f"{name:15} ₹{price:7.2f} {quantity:5} ₹{total:9.2f}")

            if price > max_price:
                max_price = price
                expensive_item = name

        # Discount
        if subtotal >= 5000:
            discount_rate = 20
        elif subtotal >= 3000:
            discount_rate = 15
        elif subtotal >= 1000:
            discount_rate = 10
        else:
            discount_rate = 0

        discount = subtotal * discount_rate / 100
        amount_after_discount = subtotal - discount

        # GST
        gst = amount_after_discount * 18 / 100

        final_amount = amount_after_discount + gst

        print("----------------------------------------")
        print(f"Subtotal              : ₹{subtotal:.2f}")
        print(f"Discount ({discount_rate}%)       : -₹{discount:.2f}")
        print(f"Amount after discount : ₹{amount_after_discount:.2f}")
        print(f"GST (18%)              : ₹{gst:.2f}")
        print("----------------------------------------")
        print(f"Final Payable Amount   : ₹{final_amount:.2f}")
        print("----------------------------------------")
        print(f"Most Expensive Item    : {expensive_item}")
        print(f"Price                  : ₹{max_price:.2f}")
        print("========================================")
        print("        Thank you for shopping!")
        print("========================================")

    elif choice == 6:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")