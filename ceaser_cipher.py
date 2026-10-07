# AB, Caeser Cipher.py

def caesar_shift(message, shift):
    result = ""

    for letter in message:
        number = ord(letter)
        new_number = number + shift

        if letter >= "A" and letter <= "Z":
            if new_number > ord("Z"):
                new_number = new_number - 26

            new_letter = chr(new_number)

        elif letter >= "a" and letter <= "z":
            if new_number > ord("z"):
                new_number = new_number - 26

            new_letter = chr(new_number)

        else:
            new_letter = letter

        result = result + new_letter

    return result


print(caesar_shift("Khoor", -3))

choice = input("Do you want to (E)ncrypt or (D)ecrypt? ")
message = input("Enter your message: ")
shift = int(input("Enter the shift amount: "))

if choice == "E" or choice == "e":
    result = caesar_shift(message, shift)
    print("Encrypted message:", result)

elif choice == "D" or choice == "d":
    result = caesar_shift(message, -shift)
    print("Decrypted message:", result)