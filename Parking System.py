totalslots = 1000
vehical_parked = 425

while True:
    print("================================================")
    print("              LNT PARKING SYSTEM")
    print("================================================")
    print("Press 1 to park your vehical")
    print("Press 2 to show the no of vehical parked")
    print("Press 3 to show the price of vehical to park")
    print("Press 4 to show the available slots")
    print("Press 5 to exit")
    print("================================================")

    c = int(input("Enter the choice: "))

    if c == 1:
        print("\nEnter the vehical no:")
        input()

        print("Enter the hours of parking:")
        a = int(input())

        print("Enter the vehical type:")
        b = int(input())

        if b == 2:
            price = 25
            print("Price =", price * a)
        elif b == 3:
            price = 35
            print("Price =", price * a)
        elif b == 4:
            price = 50
            print("Price =", price * a)
        elif b == 8:
            price = 90
            print("Price =", price * a)
        else:
            print("Invalid vehical")

    elif c == 2:
        print("\nTotal no of vehical parked:", vehical_parked)

    elif c == 3:
        print("\nEnter the vehical type (wheeler):")
        a = int(input())

        if a == 2:
            print("Price = 25")
        elif a == 3:
            print("Price = 35")
        elif a == 4:
            print("Price = 50")
        elif a == 8:
            print("Price = 90")
        else:
            print("Invalid vehical")

    elif c == 4:
        print("\nTotal Slots:", totalslots)
        print("Occupied Slots:", vehical_parked)
        print("Available Slots:", totalslots - vehical_parked)

    elif c == 5:
        print("\nThank You for using LNT Parking System!")
        break

    else:
        print("Invalid Choice!")
