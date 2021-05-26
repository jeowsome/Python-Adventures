import math

num = int(input())

edge = round(2 * (math.sqrt(3)) * (num ** 2), 2)
length = round((1 / 3) * (math.sqrt(2)) * (num ** 3), 2)

print(edge, length)