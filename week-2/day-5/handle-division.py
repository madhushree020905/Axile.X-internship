try:
    number=int(input("Enter a number: "))
    divisor=int(input("Enter divisor: "))

    result=number/divisor
    print("Division Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input! Enter numbers only.")

finally:
    print("execution completed.")