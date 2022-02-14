import os

from colorama import Fore
import pickle, random, os

yellow, green, red, reset = Fore.YELLOW, Fore.GREEN, Fore.RED, Fore.RESET

wordlist = tuple(pickle.load(open("words list.dat", 'rb')))
wordleword = random.choice(wordlist)
string = ''
while True:
    os.system('cls')
    print(string)
    userinp = input(">>")
    if len(userinp) != 5: input("Word size is not 5. Try again by pressing 'ENTER KEY':")
    else:
        if wordleword == userinp:
            print("You guessed it right!!!!\n"
                  "The word is", wordleword)
            break
        else:
            string += '\n'
            colorword = ''
            for index, letter in enumerate(userinp):
                if wordleword[index] == letter:
                    string += green + letter + reset
                    colorword += letter
                elif letter in wordleword:
                    if colorword.count(letter) < wordleword.count(letter):
                        string += yellow + letter + reset
                        colorword += letter
                    else:
                        string += letter
                else:
                    string += red + letter + reset
