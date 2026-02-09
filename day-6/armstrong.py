num=int(input("Enter a number:"))
s=0
t=num
while t>0:
    d=t%10
    s+=d**3
    t//=10

if s==num:
    print("It is Armstrong")
else:
    print("It is not Armstrong")
