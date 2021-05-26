import math

num1 = int(input())
num2 = int(input())

if num2 <= 1:
    print(round(math.log(num1), 2))
else:
    print(round(math.log(num1, num2), 2))