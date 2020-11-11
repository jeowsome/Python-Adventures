texts = input().split(' ')
word = []
to_check = ('www.', 'http')

for text in texts:
    if text.lower().startswith(to_check):
        print(text)
