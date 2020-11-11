# put your python code here
words = input().split()
equivalent = 0.0

for word in words:
    if 'A' in word:
        equivalent += 1.0

print(round(equivalent / len(words), 2))
