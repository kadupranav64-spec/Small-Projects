# Movie Ticket Booking System

movies = {
    "Inception": {"price": 200, "tickets": 50},
    "Interstellar": {"price": 180, "tickets": 40},
    "Joker": {"price": 220, "tickets": 30}
}

bookings = []

while True:
    print("\n===== Movie Ticket Booking System =====")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. Count Booked Tickets")
    print("4. View Bookings")
    print("5. Check Tickets Left")
    print("6. Ticket Price Per Movie")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nAvailable Movies:")
        for movie in movies:
            print(movie)

    elif choice == 2:
        movie = input("Enter movie name: ")

        if movie in movies:
            qty = int(input("How many tickets? "))

            if qty <= movies[movie]["tickets"]:
                movies[movie]["tickets"] -= qty
                total = qty * movies[movie]["price"]

                bookings.append({
                    "movie": movie,
                    "tickets": qty,
                    "amount": total
                })

                print("Booking Successful!")
                print("Total Amount =", total)
            else:
                print("Not enough tickets available.")
        else:
            print("Movie not found.")

    elif choice == 3:
        total_tickets = 0
        for booking in bookings:
            total_tickets += booking["tickets"]

        print("Total Booked Tickets:", total_tickets)

    elif choice == 4:
        if len(bookings) == 0:
            print("No bookings yet.")
        else:
            print("\nBooking Details:")
            for booking in bookings:
                print("Movie:", booking["movie"])
                print("Tickets:", booking["tickets"])
                print("Amount:", booking["amount"])
                print("-----------------------")

    elif choice == 5:
        print("\nTickets Left:")
        for movie in movies:
            print(movie, ":", movies[movie]["tickets"])

    elif choice == 6:
        print("\nTicket Prices:")
        for movie in movies:
            print(movie, ":", movies[movie]["price"])

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
