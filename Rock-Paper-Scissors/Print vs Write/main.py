numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file_name = open('file_with_list.txt', 'w')

print(str(numbers), end='', file=file_name)

file_name.close()