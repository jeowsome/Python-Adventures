import math

num = int(input())
num = math.radians(num)

print(round(math.cos(num) / math.sin(num), 10))
