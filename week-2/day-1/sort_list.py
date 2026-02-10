numbers=input("Enter the numbers:")
list=list(map(int, numbers.split()))

list.sort()
print("The Ascending order is:",list)

list.sort(reverse=True)
print("The Descending order is:",list)
