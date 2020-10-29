word = input()
special = ["*", "_", "~", "`"]

for i in word:
    if i in special:
        word = word.strip(i)

print(word)
