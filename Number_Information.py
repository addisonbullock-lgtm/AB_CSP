# AB Number Information

# Loop through numbers 1 to 20 inclusive
for num in range(1, 21):
    #Even or Odd
    if num % 2 == 0:
        # Inner (nested) check for Even numbers: Divisible by 5?
        if num % 5 == 0:
            print(f"{num} is even and divisible by 5")
        else:
            print(f"{num} is even and not divisible by 5")
    else:
        # Inner (nested) check for Odd numbers: Divisible by 5?
        if num % 5 == 0:
            print(f"{num} is odd and divisible by 5")
        else:
            print(f"{num} is odd and not divisible by 5")