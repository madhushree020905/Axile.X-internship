num=int(input("Enter a number: "))
temp=num
rev=0

while num>0:
    rev=rev*10+(num%10)
    num=num//10

if temp==rev:
    print("It is a Palindrome number")
else:
    print("It is not a palindrome")
