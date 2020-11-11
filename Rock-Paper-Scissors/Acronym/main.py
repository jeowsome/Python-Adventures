# read test.txt
test = open('test.txt', 'r')

for word in test:
    print(word[0])

test.close()