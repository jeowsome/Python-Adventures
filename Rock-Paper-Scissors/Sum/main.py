# read sums.txt
file = open('sums.txt', 'r')

for stuff in file:
    print(int(stuff.split()[0]) + int(stuff.split()[1]))

file.close()