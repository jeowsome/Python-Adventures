words = input().split()
duplicates = []
for word in words:
    if word[-1] == 's':
        duplicates.append(word)

print('_'.join(duplicates))