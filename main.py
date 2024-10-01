import sys
import string
import random

#needed for shift
alphabet = {letter: index for index, letter in enumerate(string.ascii_letters, start=0)}
indices = {index: letter for letter, index in alphabet.items()}

#needed for permutation
numbers = list(range(1,53))
shuffled_alphabet = list(alphabet)
random.shuffle(shuffled_alphabet)
#default key permutation
permuted_alphabet = {original: permuted for original, permuted in zip(alphabet, shuffled_alphabet)}


def shiftCipher():
    choice = input("1) Encryption \n2) Decryption ")
    #encryption
    if choice == "1":
        plainText = input("Enter the plaintext: ")
        if plainText == "":
            return print("ERROR: no plaintext detected.")
        keyChoice = input("1) Encryption Key \n2) Default key ")
        if keyChoice == "":
            print("ERROR: no key detected")
        elif keyChoice == "1":
            key = int(input("Enter encryption key: "))
        elif keyChoice == "2":
            print("Default key will be used.")
            key = 5
        
        cipherText = ""

        for letter in plainText:
            
            if letter in alphabet:
                shiftedPosition = (alphabet[letter] + key) % 52  # new position is alphabet position + key; % is for the edge case of letters towards the end so that it can wrap back around
                #Case-follow (QoL)

                #add shifted letter to ciphertext, if upper keep but if lower then make lowercase
                if letter.isupper():
                    cipherText += indices[shiftedPosition] 
                else:
                    cipherText += indices[shiftedPosition].lower()
            else:
                cipherText += letter # non-alphabet characters edge case

        print("Ciphertext: " + cipherText)
    #decryption
    elif choice == "2":
        #reverse of encryption but instead decrement in the shifted position. 
        cipherText = input("Enter ciphertext: ")
        if cipherText == "":
            return print("No text inputted.")
        keyChoice = input("1) Encryption Key \n2) Default key ")
        if keyChoice == "":
            print("ERROR: no key detected")
        elif keyChoice == "1":
            key = int(input("Enter encryption key: "))
        elif keyChoice == "2":
            key = 5
            print("Default key will be used.")
        plainText = ""
        #enumerate through plaintext and print out the letters in its positions + key shift (relative to the alphabet mapping)

        for letter in cipherText:
            
            if letter in alphabet:
                shiftedPosition = (alphabet[letter] - key) % 52  # new position is alphabet position + key; % is for the edge case of letters towards the end so that it can wrap back around
                #Case-follow (QoL)

                #add shifted letter to ciphertext, if upper keep but if lower then make lowercase
                if letter.isupper():
                    plainText += indices[shiftedPosition] 
                else:
                    plainText += indices[shiftedPosition].lower()
            else:
                plainText += letter # non-alphabet characters edge case

        print("Plaintext: " + plainText)
    else: 
        print("ERROR: choice not detected. Please try again.")


def permCipher():
    choice = input("1) Encryption \n2) Decryption ")
    if choice == "1":
        plainText = input("Enter the plaintext: ")
        if plainText == "":
            return print("ERROR: no plaintext detected.")
        keyChoice = input("1) Encryption Key \n2) Default key ")
        if keyChoice == "":
            print("ERROR: no key detected")
        elif keyChoice == "1":
            key = int(input("Enter encryption key (permuted alphabet of choice): "))
        elif keyChoice == "2":
            key = permuted_alphabet
            print("Default key will be used.")
        
        cipherText = ""
        #enumerate through plaintext and print out the letters in its positions + key shift (relative to the alphabet mapping)

        for letter in plainText:
            
            if letter in alphabet:  
                if key[letter].isupper():
                    cipherText += key[letter]
                else: 
                    cipherText += (key[letter]).lower()
            else:
                cipherText += letter # non-alphabet characters edge case

        print("Sanity check: \nPermuted alphabet: " + str(key))
        print("Ciphertext: " + cipherText)
    elif choice == "2":
        #reverse of encryption but instead decrement in the shifted position. 
        cipherText = input("Enter ciphertext: ")
        if cipherText == "":
            return print("No text inputted.")
        keyChoice = input("1) Encryption Key \n2) Default key ")
        if keyChoice == "":
            print("ERROR: no key detected")
        elif keyChoice == "1":
            key = int(input("Enter encryption key (permuted alphabet of choice): "))
        elif keyChoice == "2":
            key = permuted_alphabet

        plainText = ""

        for letter in cipherText:
            if letter in alphabet: 
                if key[letter].isupper():
                    plainText += key[letter]
                else: 
                    plainText += (key[letter]).lower()
            else:
                plainText += letter

        print("Sanity check: \nPermuted alphabet: " + str(key))
        print("Plaintext: " + plainText)

    else: 
        print("ERROR: choice not detected. Please try again.")

    # print(permuted_alphabet)

def simpleTransp():
    choice = input("1) Encryption \n2) Decryption ")
    if choice == "1":
        plainText = input("Enter plaintext: ")
        plainText = plainText.replace(" ", "")
        keyChoice = input("1) Encryption Key \n2) Default key ")
        if keyChoice == "":
            print("ERROR: no key detected")
        elif keyChoice == "1":
            key = (input("Enter key: "))
        elif keyChoice == "2":
            key = "HACK"

        while len(plainText) % len(key) != 0:
            plainText += "X"

        keyOrder = sorted(list(key))
        columns = len(key)
        rows = len(plainText) // columns
        matrix = [plainText[i * columns:(i + 1) * columns] for i in range(rows)]

        transposed = ''
        for k in keyOrder:
            index = key.index(k)
            for row in matrix:
                transposed += row[index]

        print("Ciphertext: " + transposed)
    elif choice == "2":
        cipherText = input("Enter ciphertext: ")
        keyChoice = input("1) Encryption Key \n2) Default key ")
        if keyChoice == "":
            print("ERROR: no key detected")
        elif keyChoice == "1":
            key = (input("Enter key: "))
        elif keyChoice == "2":
            key = "HACK"
        columns = len(key)
        rows = len(cipherText) // columns
        matrix = ['' for _ in range(columns)]
        keyOrder = sorted(list(key))
        
        current_index = 0
        for k in keyOrder:
            col_index = key.index(k)
            matrix[col_index] = cipherText[current_index:current_index + rows]
            current_index += rows

        plainText = ""
        for i in range(len(matrix[0])):
            for col in matrix:
                plainText += col[i]
        
        print("Plaintext: " + plainText)
    else: 
        print("ERROR: choice not detected. Please try again.")

def doubleTransp():
    choice = input("1) Encryption \n2) Decryption ")
    if choice == "1":
        plainText = input("Enter plaintext: ")
        plainText = plainText.replace(" ", "")
        keyChoice = input("1) Encryption Key \n2) Default key ")
        if keyChoice == "":
            print("ERROR: no key detected")
        elif keyChoice == "1":
            key1 = (input("Enter key 1: "))
            key2 = (input("Enter key 2: "))
        elif keyChoice == "2":
            key1 = "HACK"
            key2 = "CODE"

        while len(plainText) % len(key1) != 0:
            plainText += "X"

        keyOrder1 = sorted(list(key1))
        columns = len(key1)
        rows = len(plainText) // columns
        matrix = [plainText[i * columns:(i + 1) * columns] for i in range(rows)]

        transposed = ''
        for k in keyOrder1:
            index = key1.index(k)
            for row in matrix:
                transposed += row[index]

        keyOrder2 = sorted(list(key2))
        columns = len(key2)
        rows = len(plainText) // columns
        matrix = [plainText[i * columns:(i + 1) * columns] for i in range(rows)]

        transposed = ''
        for k in keyOrder2:
            index = key2.index(k)
            for row in matrix:
                transposed += row[index]

        print("Ciphertext: " + transposed)
    elif choice == "2":
        cipherText = input("Enter ciphertext: ")
        keyChoice = input("1) Encryption Key \n2) Default key ")
        if keyChoice == "":
            print("ERROR: no key detected")
        elif keyChoice == "1":
            key1 = (input("Enter key 1: "))
            key2 = (input("Enter key 2: "))
        elif keyChoice == "2":
            key1 = "HACK"
            key2 = "CODE"

        columns1 = len(key2)
        rows1 = len(cipherText) // columns1

        matrix1 = ['' for _ in range(columns1)]
        current_index = 0
        keyOrder2 = sorted(list(key2))

        for k_2 in keyOrder2:
            col_index = key2.index(k_2)
            matrix1[col_index] = cipherText[current_index:current_index + rows1]
            current_index += rows1
        
        incompletePT = ""
        for i in range(rows1):
            for col in matrix1:
                incompletePT += col[i]

        columns2 = len(key1)
        rows2 = len(incompletePT) // columns2

        matrix2 = ['' for _ in range(columns2)]
        current_index = 0
        keyOrder1 = sorted(list(key1))

        for k_1 in keyOrder1:
            col_index = key1.index(k_1)
            matrix2[col_index] = incompletePT[current_index:current_index + rows2]
            current_index += rows2

        plainText = ""
        for i in range(rows2):
            for col in matrix2:
                plainText += col[i]
        print("Plaintext: " + plainText)
        
    else:
        print("ERROR: choice not detected. Please try again.")


def vignere():
    pass

def encAlgo():
    pass

def encMode():
    pass 

if len(sys.argv) != 2:
    print("ERROR: Not enough/too many input arguments.")
    sys.exit(1)

#enter command line in this fashion: 
#py main.py (option)
#where 1 is substitution
#2 is transposition
#3 is vigenere
#4 is diff encryption algorithm
#5 is diff encryption modes

option = ""

firstArgument = sys.argv[1]
match firstArgument: 
    case "1":
        choice = input("1) Shift Cipher \n2) Permutation Cipher ")
        if choice == "1":
            shiftCipher()
        elif choice == "2":
            permCipher()
        else:
            print("ERROR: Out of index, please try again with number 1/2")
    case "2":
        choice = input("1) Simple Transposition \n2) Double Transposition ")
        if choice == "1":
            simpleTransp()
        elif choice == "2":
            doubleTransp()
        else:
            print("ERROR: Out of index, please try again with number 1/2")
    case "3":
        vignere()
    case "4":
        encAlgo()
    case "5":
        encMode()
    case _:
        print("ERROR: Out of index, please enter number 1-5")




