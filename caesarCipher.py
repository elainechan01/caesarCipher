"""
Program to implement Caesar Cipher
"""

def quit_program():
    invalidValue = True
    while invalidValue:
        userInput = input("Quit? (y/n): ")
        if userInput.lower() == "y":
            return True
        elif userInput.lower() == "n":
            return False
        else:
            print("Invalid value.")

def get_user_input():
    userInput = input("\nEnter your string here: ")
    return userInput

def get_shift():        # CHALLENGE PORTION
    invalidValue = True
    while invalidValue:
        userInput = input("Enter shift value here: ")
        try:
            return int(userInput)
        except ValueError:
            print("Invalid value.")

def split_ascii(word):               
    return [char for char in word]

def changeCharacter(char, shift, alphabet):
    isCaps = False
    if char.isupper():
        isCaps = True
        char = char.lower()
    if char in alphabet:
        charCurrentIndex = alphabet.index(char)
        charNewIndex = charCurrentIndex + shift
        while charNewIndex < 0 or charNewIndex > 25:
            if charNewIndex > 25:
                charNewIndex -= 26
            elif charNewIndex < 0:
                charNewIndex += 26
        newChar = alphabet[charNewIndex]
        if isCaps:
            newChar = newChar.upper()
        return newChar
    else:
        return char

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = split_ascii(alphabet)
    caesarCode = []
    quit = False
    while not quit:
        string = get_user_input()
        shift = get_shift()
        for char in string:
            newChar = changeCharacter(char, shift, alphabet_list)
            caesarCode.append(newChar)
        print("\nThe encoded message is: ")
        print(''.join(map(str, caesarCode)))
        print()
        caesarCode.clear()
        quit = quit_program()


if __name__ == "__main__":
    main()
