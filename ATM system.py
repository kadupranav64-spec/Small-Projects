balance = 12000
pin = 2101

input("Enter your card: ")

print("!!!!!!!!!!! Welcome to the ATM !!!!!!!!!!!")
print("Press 1 to check balance")
print("Press 2 to get mini Statement")
print("Press 3 to deposit money")
print("Press 4 to withdraw money")
print("Press 5 to change the pin")
print("Press 6 to exit")

c = input("Enter your choice: ")

if c == "1":
    input("Enter card type: ")
    a = input("Enter account type: ")

    if a == "saving":
        b = int(input("Enter your pin: "))

        if b == pin:
            print(balance)
        else:
            print("Invalid pin")
    else:
        print("Invalid account type")


elif c == "2":
    input("Enter card type: ")
    a = input("Enter account type: ")

    if a == "saving":
        b = int(input("Enter your pin: "))

        if b == pin:
            print(balance)
        else:
            print("Invalid pin")
    else:
        print("Invalid account type")


elif c == "3":
    input("Enter card type: ")
    a = input("Enter account type: ")

    if a == "saving":
        b = int(input("Enter the amount you want to deposit: "))
        c = int(input("Enter your pin: "))

        if c == pin:
            balance += b
            print(balance)
        else:
            print("Invalid pin")
    else:
        print("Invalid account type")


elif c == "4":
    input("Enter card type: ")
    a = input("Enter account type: ")

    if a == "saving":
        b = int(input("Enter the amount you want to withdraw: "))
        c = int(input("Enter your pin: "))

        if c == pin:
            if balance < b:
                print("Insufficient balance")
            else:
                balance -= b
                print(balance)
        else:
            print("Invalid pin")
    else:
        print("Invalid account type")


elif c == "5":
    input("Enter card type: ")
    a = int(input("Enter your pin: "))

    if a == pin:
        b = int(input("Enter the new pin: "))
        pin = b
        print("Pin changed successfully")
    else:
        print("Invalid pin")


elif c == "6":
    print("Transaction ended")


else:
    print("Invalid choice")
