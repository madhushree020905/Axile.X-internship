students={}

while True:
    print("\n 1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice=input("Enter the choice: ")

    if choice=="1":
        usn=input("Enter USN: ")
        name=input("Enter Name: ")
        dept=input("Enter department: ")
        marks=input("Enter Marks: ")
        students[usn]={"Name": name, "Department": dept, "Marks": marks}
        print("Student Added Successfully!")

    elif choice=="2":
        for roll,details in students.items():
            print("USN:", roll)
            print("Name:", details["Name"])
            print("Department:", details["Department"])
            print("Marks:", details["Marks"])
            print("------")

    elif choice == "3":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice!")
