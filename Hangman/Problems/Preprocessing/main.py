word = input()
punctuations = [",", "!", "?", "."]

for i in word:
    if i in punctuations:
        word = word.replace(i, "")

print(word.lower())