# AB - Number Guessing Game

import random

# The secret number will be between 1 and 100
secret_number = random.randint(1, 100)

# The player gets 6 guesses
max_guesses = 6

print("I'm thinking of a number between 1 and 100. You have 6 tries to guess it.")

for attempt in range(1, max_guesses + 1):
    guess = int(input("Guess #" + str(attempt) + ": "))
    if guess < secret_number:
        print(" Wrong, Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Congratulations!, You shall pass! You guessed the number in " + str(attempt) + " tries.")
        break

else:
    print("Sorry, you shall not pass, high school. The number was " + str(secret_number) + ".")