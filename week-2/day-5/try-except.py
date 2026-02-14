try:
    number1=int(input("Enter first number:"))
    number2=int(input("Enter second number:"))

    sum=number1+number2
    difference=number1-number2
    product=number1*number2

    print("Addition:", sum)
    print("Subtraction:", difference)
    print("Multiplication:", product)

except ValueError:
    print("Error. Please enter only integer values.")