def check_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print("This is a Prime number")
    else:
        print("This is not a prime number")
num=int(input("Enter a number:"))
check_prime(num)