score = int(input())
test_max = int(input())
score = (score / test_max) * 100

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score < 60:
    print("F")
