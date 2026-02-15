balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        print("Current Balance:", balance)

    elif choice=="2":
        amount=float(input("Enter amount to deposit: "))
        balance+=amount
        print("Amount Deposited")

    elif choice=="3":
        amount=float(input("Enter amount to withdraw: "))
        if amount<=balance:
            balance-=amount
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    elif choice=="4":
        print("Thank You")
        break

    else:
        print("Invalid Option")