string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0

for letter in vowels:
    for let in string:
        if letter == let:
            count += 1

print(count)
