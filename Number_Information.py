# AB Number Information

# Loop through numbers 1 to 20

for count in range(1, 21):

#Test if even looking
    if count % 2 == 0:
#Test if divisible by 5
        if count % 5 == 0:
            print(str(count) + " is even looking and divisible by 5")
        else:
            print(str(count) + " is even looking and not divisible by 5")          
    else:
        #Test if odd looking and divisible by 5
        if count % 5 == 0:
            print(str(count) + " is odd looking and divisible by 5")
        else:
            print(str(count) + " is odd and not divisible by 5")
