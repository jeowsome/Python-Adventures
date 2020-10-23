word = input()
s = ""

for char in word:
    if char.islower():
        s += char
    else:
        s += "_" + char.lower()

print(s)

