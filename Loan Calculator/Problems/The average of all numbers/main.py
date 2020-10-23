# put your python code here
a = int(input())
b = int(input())
num = []

for i in range(a, b + 1):
    if i % 3 == 0:
        num.append(i)


print(sum(num) / len(num))
