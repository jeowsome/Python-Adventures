import random

# Write your code here
# Output a line Enter your name: . Note that the user should enter his/her name on the same line
match = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree',
         'human', 'snake', 'scissors', 'fire']
beats_rock = match[1:8]
beats_fire = match[0:7]
beats_scissors = match[5:]
beats_snake = match[4:-1]
beats_human = match[3:-2]
beats_tree = match[2:-3]
beats_wolf = match[1:-4]
beats_sponge = match[0:-5]
beats_paper = match[8:]
beats_air = match[7:-1]
beats_water = match[6:-2]
beats_dragon = match[5:-3]
beats_devil = match[4:-4]
beats_lightning = match[3:-5]
beats_gun = match[2:-6]

player_name = input("Enter your name: ")

# Read input specifying the user's name and output a new line Hello, <name>
print("Hello,", player_name)

# Read a file named rating.txt
score = open('rating.txt', 'r')


# check if there's a record for the user with the same name
for lines in score.readlines():
    # if yes, use the score specified in the rating.txt for this user
    # as a starting point for calculating the score in the current game
    if player_name in lines.split():
        score = int(lines.split()[1])
        break
    else:
        # If no, start counting user's score from 0.
        score = 0

user_option = input().split()

# Read input specifying the list of options that will be used for playing the game
if user_option:
    options = user_option
    # If the input is an empty line, play with default options.
else:
    options = ["rock", "paper", "scissors"]

print(options)

# Output a line Okay, let's start
print("Okay, let's start")
running = True

while running:
    option = random.choice(options)
    user = input()
    if user == option :
        print(f"There is a draw ({option})")
        score += 50
    elif user == "rock":
        if option not in beats_rock:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else:
            print(f"Sorry, but the computer chose {option}")
    elif user == "paper":
        if option in beats_paper:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "scissors":
        if option in beats_scissors:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "snake":
        if option in beats_snake:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "human":
        if option in beats_human:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "tree":
        if option in beats_tree:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "wolf":
        if option in beats_wolf:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "sponge":
        if option in beats_sponge:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "air":
        if option in beats_air:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "water":
        if option in beats_water:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "dragon":
        if option in beats_dragon:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "devil":
        if option in beats_devil:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "lightning":
        if option in beats_lightning:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "gun":
        if option in beats_gun:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "fire":
        if option in beats_fire:
            print(f"Well done. The computer chose {option} and failed")
            score += 100
        else :
            print(f"Sorry, but the computer chose {option}")
    elif user == "!exit" :
        print("Bye!")
        running = False
    elif user == "!rating" :
        print("Your rating:", score)
    else :
        print("Invalid input")
