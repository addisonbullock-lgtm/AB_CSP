# AB Number Guessing Game

import random

#Game Settings:
#Range: 1 to 100
#Attemps limit: 6 tries
secret_number= random.randint(1, 100)
max_attempts= 6

(f"I'm thinking of a number between 1 and 100. You have {max_attempts} tries to guess it.")

# Loop to control the number of guess attempts
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Guess #{attempt}: "))
    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print(f"Congratulations! You guessed the number in {attempt} tries.")
        break
else:
    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")