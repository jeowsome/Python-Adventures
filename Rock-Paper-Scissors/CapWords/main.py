words = input().split('_')
result = []
for word in words:
    result.append(word.capitalize())

print(''.join(result))