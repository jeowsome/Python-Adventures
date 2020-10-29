a = int(input())
b = int(input())
h = int(input())

if h < a:
    print('Deficiency')
elif h > b:
    print('Excess')
elif a <= h <= b:
    print('Normal')
