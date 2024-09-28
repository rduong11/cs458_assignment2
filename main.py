import sys

def shiftCipher():
    pass 

def permCipher():
    pass

def simpleTransp():
    pass 

def doubleTransp():
    pass

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
        choice = input("1) Shift Cipher \n 2) Permutation Cipher")
        if choice == 1:
            shiftCipher()
        elif choice == 2:
            permCipher()
        else:
            print("ERROR: Out of index, please try again with number 1/2")
    case "2":
        choice = input("1) Simple Transposition \n 2) Double Transposition")
        if choice == 1:
            simpleTransp()
        elif choice == 2:
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




