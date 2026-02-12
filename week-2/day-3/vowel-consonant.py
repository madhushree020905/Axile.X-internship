text=input("Enter a string: ")

vowel=0
consonant=0

for char in text.lower():
    if char in "aeiou":
        vowel+=1
    elif char >= 'a' and char <= 'z':
        consonant+=1
print("Vowels:", vowel)
print("Consonants:", consonant)