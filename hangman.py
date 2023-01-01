import random

def hangman(word):
    wrong = 0
    letters = list(word)

    stages = ["--------",
              "    O   ",
              "   /|\  ",
              "    |   ",
              "   / \  ",
              "        "]
    
    board = ["_"] * len(word)
    win = False

    print("Welcome to hangman!")

    while wrong < len(stages) - 1:
        character = input("Guess a character")
        if character in word:
            charIndex = letters.index(character)
            board[charIndex] = character
        else:
            wrong += 1
            for i in range(wrong):
                print(stages[i])
        print(" ".join(board))
        if "_" not in board:
            print("You Win!")
            win = True
            print(" ".join(board))
            break       
    if not win:
        print("You Lost!")
        print("The word was " + word)  


words = ["ironman", "thor", "hulk", "drstrange", "spiderman"]
num = random.randint(0,len(words))
hangman(words[num])
