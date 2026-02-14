class AgeValidError(Exception):
    pass
try:
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))

    if age<0:
        raise AgeValidError("Age cannot be negative.")

    elif age<18:
        raise AgeValidError("You are not eligible to apply.")

    else:
        print("Name:", name)
        print("Age:", age)
        print("Status: Eligible")

except AgeValidError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Invalid input! Please enter numeric value for age.")

finally:
    print("Program finished.")
