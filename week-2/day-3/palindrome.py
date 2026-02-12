text=input("Enter the string:")

reverse_text=""
for char in text:
    reverse_text=char+reverse_text

if text==reverse_text:
    print("It is Palindrome")
else:
    print("It is not Palindrome")
