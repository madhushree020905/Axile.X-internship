sentence=input("Enter a sentence: ")
words=sentence.split()

word_count={}

for w in words:
    if w in word_count:
        word_count[w]=word_count[w]+1
    else:
        word_count[w]=1

print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)
