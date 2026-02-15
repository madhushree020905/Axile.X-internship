while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        name=input("Enter your Name: ")
        marks=input("Enter your Marks: ")

        file=open("records.txt", "a")
        file.write(name + " - " + marks + "\n")
        file.close()

        print("Record Saved")

    elif choice=="2":
        try:
            file=open("records.txt", "r")
            print(file.read())
            file.close()
        except:
            print("No records found.")

    elif choice=="3":
        break

    else:
        print("Invalid Choice")
