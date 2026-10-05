# AB, hangman.py

with open("words.txt", "r") as file:
    words= file.read(split("words.txt, r"))
    connect= file.game()
    connect= connect + "hangman"
    print(connect)

with open("hangman.txt", "w") as file:
    file.game("Hangman")

# Creating the game

import random

#Secret word would be A through Z
secret_word= random.randint(A,Z)

#The player gets 6 guesses
max_guesses= 6
print("We are playing hangman, I'm thinking of a word between A and Z. You have 6 tries to guess it")

for attempt in range(1, max_guesses + 1):
    guess= int(input("Guess #" + str(attempt) + ": "))
    if guess < secret_word:
        print("Wrong word dude")
    elif guess > secret_word:
        print("Wrong word dude")
    else:
        print("Hooray! YOU GOT THE WORD in " + str(attempt) + tries)
        break

else:
    print("Sorry, you guessed the word wrong, the word was " + str(secret_word) + ".")