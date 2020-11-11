count = int(input())
triangle = []

for i in range(1, count + count, 2):
    word = '#' * i
    print(word.center(count + count))
