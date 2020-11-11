# put your python code here
numbers = input().split(' ')  # read the input then create a new list for positions
to_find = input()
to_print = []

# when "iterating over the list of numbers", append all the found occurrences
for i in range(len(numbers)):
    if numbers[i] == to_find:
        to_print.append(str(i))

# Finally, join the list of indexes or print the message "not found".
if to_print:
    print(' '.join(to_print))
else:
    print("not found")
