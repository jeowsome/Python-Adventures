# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
life = 8
dashed = "-" * len(word)
print("H A N G M A N")
dashed = list(dashed)
mystery = ""
status = ""
game = True
wrongs = []
mode = ["play", "exit"]
option = ""

while option not in mode:
    option = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if option == mode[0]:
        while game:
            if word == mystery.join(dashed):
                status = "You guessed the word!"
                game = False
            print()
            print(mystery.join(dashed))
            guess = input("Input a letter: ")
            if guess in word:
                status = ""
                if guess in dashed:
                    print("You already typed this letter")
                elif word.count(guess) == 1:
                    dashed[word.find(guess)] = guess
                elif word.count(guess) > 1:
                    dashed[word.find(guess)] = guess
                    dashed[word.rfind(guess)] = guess
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
                    if life == 0:
                        game = False
                print(status)
            if word == mystery.join(dashed):
                status = "You guessed the word!"
                game = False
        else:
            if life != 0:
                print("You survived!")
            else:
                print("You lost!")

    elif option == mode[1]:
        quit()
