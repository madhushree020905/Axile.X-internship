contacts={}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. View All")
    print("4. Exit")

    choice=input("Enter choice: ")

    if choice=="1":
        name=input("Enter Name: ")
        phone=input("Enter Phone Number: ")
        contacts[name]=phone
        print("Contact Saved")

    elif choice=="2":
        name=input("Enter Name to Search: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact Not Found")

    elif choice=="3":
        print("All Contacts:", contacts)

    elif choice=="4":
        break

    else:
        print("Invalid Choice")
