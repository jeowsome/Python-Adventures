n = int(input())
num = []

for _ in range(n):
    n = int(input())
    num.append(n)

print(sum(num) / len(num))