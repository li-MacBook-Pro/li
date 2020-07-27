try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *

import time
import sys
import os
import random

flashcards = {}


def Flashcards(key, trans, PoS):
    if not key in flashcards:
        flashcards[key] = [[trans], [PoS]]
    else:
        x = []
        for item in flashcards[key][0]:
            x.append(item)
        x.append(trans)
        flashcards[key][0] = x
        x = []
        for item in flashcards[key][1]:
            x.append(item)
        x.append(PoS)
        flashcards[key][1] = x


def ImportGaeilge():
    flashcards = {}
    with open('gaeilge_flashcard_mode.txt','r', encoding='utf8') as file:
        for line in file:
            line1 = line.rstrip().split("=")
            key = line1[0]
            trans = line1[1]
            PoS = line1[2]
            Flashcards(key, trans, PoS)

def Gaeilge():
    numberCorrect = 0
    totalCards = 0
    ImportGaeilge()
    wrongCards = {}
    x = input('Hit "ENTER" to begin. (Type "quit" to quit)')
    while x != quit:
        os.system('cls')
        time.sleep(1.3)
        card = flashcards.popitem()
        if card == "":
## WRONG CARDS
            print ("Deck one complete.")
            Gaeilge()
        print("\n\n")
        print(str(card[0])+":")
        x = input("\t:")
        if x == 'quit':
            break
        else:
            right = False
            for item in card[1]:
                if x == card[1]:
                    right = True
                    print("\nCorrect!")
                    numberCorrect += 1
            if right == False:
                print(card[0])

        totalCards += 1
        print("Correct answers:", str(numberCorrect) +"/"+str(totalCards))


Gaeilge()




#
# gaeilge_flashcard_mode.txt：
#
# I=mé=(pron) (emphatic)
# I=mise=(n/a)
# you=tú=(pron) (subject)
# you=tusa=(emphatic)
# y'all=sibh=(plural)
# y'all=sibhse=(emphatic)
# he=sé=(pron)
# he=é=(n/a)
# he=seisean=(emphatic)
# he=eisean=(n/a)
# she=sí=(pron)
# she=í=(n/a)
# she=sise=(emphatic)
# she=ise=(emphatic)
# him=é=(pron)
# him=eisean=(emphatic)
# her=í=(pron)
# her=ise=(emphatic)
# her=a=(adj)