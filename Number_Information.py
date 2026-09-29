# AB Number Information

for num in range(1, 21):
    if num % 2 == 0:
        if num % 5 == 0:
            print(str(num) + " is even and divisible by 5.")
        else:
            print(str(num) + " is even and not divisible by 5.")
    else:
            if num % 5 == 0:
                print(str(num) + " is strange and divisible by 5.")
            else:
                print(str(num) + " is strange and not divisible by 5.")