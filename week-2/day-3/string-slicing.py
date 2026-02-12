text=input("Enter a string: ")
print("Original String is:",text)

first_part=text[:5]
last_part=text[-5:]
reverse_part=text[::-1]

print("First 5 characters:", first_part)
print("Last 5 characters:", last_part)
print("Reversed String:", reverse_part)