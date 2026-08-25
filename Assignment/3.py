# Movie Ticket Booking System

shows = {
    1: {
        "movie": "Avengers",
        "time": "10:00 AM",
        "seats": 50,
        "revenue": 0
    },
    2: {
        "movie": "KGF",
        "time": "2:00 PM",
        "seats": 40,
        "revenue": 0
    },
    3: {
        "movie": "Pushpa",
        "time": "7:00 PM",
        "seats": 30,
        "revenue": 0
    }
}

while True:

    print("\n========== MOVIE TICKET BOOKING ==========")
    print("1. View Shows")
    print("2. Book Tickets")
    print("3. View Remaining Seats")
    print("4. View Show Revenue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # View shows
    if choice == "1":

        print("\n------------- AVAILABLE SHOWS -------------")

        for show_id, show in shows.items():
            print(
                f"{show_id}. {show['movie']} | "
                f"{show['time']} | "
                f"Seats Available: {show['seats']}"
            )

    # Book tickets
    elif choice == "2":

        print("\n------------- SELECT SHOW -------------")

        for show_id, show in shows.items():
            print(
                f"{show_id}. {show['movie']} - "
                f"{show['time']} "
                f"({show['seats']} seats available)"
            )

        try:
            show_id = int(input("Enter show number: "))

            if show_id not in shows:
                print("Invalid show!")
                continue

            show = shows[show_id]

            if show["seats"] == 0:
                print("Sorry! This show is SOLD OUT.")
                continue

            number = int(input("Enter number of tickets: "))

            # Prevent overbooking
            if number <= 0:
                print("Number of tickets must be greater than 0.")
                continue

            if number > show["seats"]:
                print(
                    f"Sorry! Only {show['seats']} seats are available."
                )
                continue

            total = 0

            print("\nSeat Categories:")
            print("1. Regular  - ₹150")
            print("2. Premium  - ₹250")
            print("3. VIP      - ₹400")

            for i in range(number):

                category = input(
                    f"\nEnter category for ticket {i + 1}: "
                ).lower()

                if category == "regular":
                    price = 150
                elif category == "premium":
                    price = 250
                elif category == "vip":
                    price = 400
                else:
                    print("Invalid category! Ticket cancelled.")
                    total = 0
                    break

                age = int(input("Enter age: "))

                # Age-based discount
                if age < 12:
                    final_price = price * 0.50
                elif age >= 60:
                    final_price = price * 0.70
                else:
                    final_price = price

                total += final_price

            else:
                # Booking successful
                show["seats"] -= number
                show["revenue"] += total

                print("\n========== BOOKING SUCCESSFUL ==========")
                print("Movie:", show["movie"])
                print("Show Time:", show["time"])
                print("Tickets:", number)
                print(f"Total Amount: ₹{total:.2f}")
                print("Remaining Seats:", show["seats"])

        except ValueError:
            print("Invalid input! Please enter numbers correctly.")

    # Remaining seats
    elif choice == "3":

        print("\n========== REMAINING SEATS ==========")

        for show_id, show in shows.items():
            print(
                f"{show['movie']} ({show['time']}) : "
                f"{show['seats']} seats"
            )

    # Revenue
    elif choice == "4":

        print("\n========== SHOW REVENUE ==========")

        for show_id, show in shows.items():
            print(
                f"{show['movie']} ({show['time']}) "
                f"-> Revenue: ₹{show['revenue']:.2f}"
            )

    # Exit
    elif choice == "5":
        print("Thank you for using Movie Ticket Booking System!")
        break

    else:
        print("Invalid choice! Please try again.")