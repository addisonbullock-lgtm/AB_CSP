import random

# Range configuration: Numbers between 1 and 100
MIN_NUM = 1
MAX_NUM = 100

# Attempt limit configuration: Player gets 6 attempts
MAX_ATTEMPTS = 6

# Generate the secret random number within the chosen range
secret_number = random.randint(MIN_NUM, MAX_NUM)

print(
    f"I'm thinking of a number between {MIN_NUM} and {MAX_NUM}. You have"
    f" {MAX_ATTEMPTS} tries to guess it!"
)

# Track the guess count
for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input(f"Guess #{attempt}: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempt} tries!")
        break
else:
    # Executes only if the loop finishes without hitting a 'break'
    print(f"You're out of guesses! The number was {secret_number}.")