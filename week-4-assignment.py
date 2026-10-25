print ("Welcome to the Vending Machine!")
balance = 200
print (f"Your balance is: {balance}p")
quit = False
while not quit:
    print ("1. Crisps - 100p")
    print ("2. Chocolate - 150p")
    print ("3. Water - 120p")
    print ("4. Quit")

    choice = input("Please select an option: ")

    if choice == "1":
        if balance >= 100:
            balance -= 100
            print ("Thank you for using the Vending Machine.")
            print (f"Your balance is: {balance}p")
        else:
            print ("Insufficient balance.")
            print (f"Your balance is: {balance}p")
    elif choice == "2":
        if balance >= 150:
            balance -= 150
            print ("Thank you for using the Vending Machine.")
            print (f"Your balance is: {balance}p")
        else:
            print ("Insufficient balance.")
            print (f"Your balance is: {balance}p")
    elif choice == "3":
        if balance >= 120:
            balance -= 120
            print ("Thank you for using the Vending Machine.")
            print (f"Your balance is: {balance}p")
        else:
            print ("Insufficient balance.")
            print (f"Your balance is: {balance}p")
    elif choice == "4":
        quit = True
        print ("Thank you for using the Vending Machine.")
    