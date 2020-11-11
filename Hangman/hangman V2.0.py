# Write your code here
import sys
import random

word_counter = 0
word_list = ['omniscient', 'tribulation', 'deuteronomy', 'crucifixion', 'blasphemy', 'falsehood', 'millstone',
             'pharisee', 'transfigure', 'wilderness', 'homosexuality']
word = word_list[word_counter]
life = 5
dashed = "-" * len(word)
print("\n\t\t----------------------- H A N G M A N v2.0 -----------------------\n\n")
dashed = list(dashed)
mystery = ""
status = ""
game = True
wrongs = []
mode = ["play", "exit"]
option = ""
times_up = ['Kaya today?', "Tagal mo phoewszz", "Ano na bes"]


def reset():
    global life
    global word
    global option
    global wrongs
    global status
    global game
    global dashed
    life = 5
    word = word_list[word_counter]
    option = ""
    wrongs = []
    status = ""
    game = True
    dashed = "-" * len(word)
    dashed = list(dashed)


def replace(gues):
    ctr = 0
    for i in word:
        if gues == i:
            dashed[ctr] = gues
        ctr += 1


while option not in mode:
    option = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if option == mode[0]:
        reset()
        while game:
            if word == mystery.join(dashed):
                status = "You guessed the word!"
                game = False
            print()
            print(mystery.join(dashed))
            guess = input("Guess a letter: ")
            if guess in word:
                status = ""
                if guess in dashed:
                    print("You already typed this letter")
                elif word.count(guess) >= 1:
                    replace(guess)
                    print("You found a letter\nLife remaining:", life)
            elif guess == "!x":
                life -= 1
                times = random.choice(times_up)
                print(f"""Time's up! {times}
Life Deducted! Life Remaining {life}""", file=sys.stderr)
            elif guess == "!pass":
                print(f"Round Skipped! Word was :{word}")
                option = ""
                game = False
            elif guess == "!exit":
                print("Bye! Thank you for playing")
                quit()
            elif guess == "!life":
                print(f"Life Remaining: {life}")
            elif guess == "!guess":
                f_guess = input("Enter full word: ")
                if f_guess == word:
                    print(f"Life remaining: {life}")
                    option = ''
                    game = False
                else:
                    print(f"EEEEEEENK!")
                    option = ''
                    life = 0
                    game = False
            elif guess not in word:
                if len(guess) != 1:
                    status = "You should input a single letter"
                elif guess.islower() is False:
                    status = "It is not an ASCII lowercase letter"
                elif not guess.isalpha():
                    status = "It is not an ASCII lowercase letter"
                elif guess in wrongs:
                    status = "You already typed this letter"
                elif guess not in wrongs:
                    status = "No such letter in the word"
                    wrongs.append(guess)
                    life -= 1
                print("Life remaining:", life)
                print(status)
            if word == mystery.join(dashed):
                game = False
            if life == 0:
                game = False
        else:
            if life != 0:
                print("You guessed the word!", word)
                print("You win")
            else:
                print("You lost!")
                print("The word is:", word)
        word_counter += 1
    elif option == mode[1]:
        quit()
