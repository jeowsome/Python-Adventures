word_num = {0: 'zero', 1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

nums = input()

for i in nums:
    if int(i) in word_num:
        print(word_num[int(i)])
