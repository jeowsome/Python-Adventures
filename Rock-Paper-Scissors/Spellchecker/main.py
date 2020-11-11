dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()
misspell = []

for word in words:
    if word in dictionary:
        continue
    else:
        misspell.append(word)

if misspell:
    print('\n'.join(misspell))
else:
    print("OK")
