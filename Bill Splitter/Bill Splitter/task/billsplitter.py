import random

# write your code here
n_friends = int(input('Enter the number of friends joining (including you):\n'))
friends = {}
if n_friends <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(n_friends):
        friends[input()] = 0

    bill = int(input("Enter the total bill value:\n"))

    lucky_one = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky_one == "Yes":
        lucky = random.choice(list(friends.keys()))
        share = round(bill / (n_friends - 1), 2)
        print(f"{lucky} is the lucky one!")
        for name in friends:
            if name == lucky:
                friends[name] = 0
            else:
                friends[name] = share
    elif lucky_one == "No":
        share = round(bill / n_friends, 2)
        for name in friends:
            friends[name] = share
        print("No one is going to be lucky")

    print(friends)

