# AB, hangman.py

import random

with open("words.txt", "r") as file:
    words= file.read().splitlines()

print(words)

#Random words

secret_word= random.choice(words)
print(secret_word)
guessed_words = []

display = []

for word in secret_word:
    display.append("_")

print(display)

guess= input("Guess a word: ").lower()
if guess in secret_word.lower():
    print("Great job, you guessed the word right, you shall pass high school!")
else:
    print("Sorry, that word is not in the word. You shall not pass high school!")
