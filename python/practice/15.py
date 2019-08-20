#reverse

text=input("input text:")
words=text.split()
for i in range(len(words)):
    print(words[len(words)-i-1],end=" ")
print()
