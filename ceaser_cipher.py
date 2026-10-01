#AB, Ceaser Cipher

# function that does both encrypting and decrypting
def caesar_shift(msg, shift):
    ans = ""
    for c in msg:
        if c.isupper():
            # upper case letters
            ans += chr((ord(c) - 65 + shift) % 26 + 65)
        elif c.islower():
            # lower case letters
            ans += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            # spaces/ puncuations stay the same
            ans += c
    return ans

# ask user for stuff
mode = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")
text = input("Enter your message: ")
s = int(input("Enter a shift amount: "))

if mode == "E" or mode == "e":
    print("Your encrypted message is:", caesar_shift(text, s))
elif mode == "D" or mode == "d":
    # flipping shift number to go backwards
    print("Your decrypted message is:", caesar_shift(text, -s))
else:
    print("Invalid choice!")