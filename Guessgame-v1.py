import string

import random

import sys

import time

def design():

    print("*" * 50)

design()

print(

    "Alright. Let's play a small guessing game!\n\nRules:\n1.Choose a category\n2.Enter a letter. You get 6 attempts\n3.Find the word\n"

)

design()

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)

category = {

    'Animals': [

        'dog', 'goat', 'pig', 'sheep', 'horse', 'camel', 'donkey', 'cat',

        'lion', 'tiger', 'elephant', 'monkey'

    ],

    'Fruits': [

        'pineapple', 'pomegranate', 'apricot', 'lemon', 'apple', 'banana',

        'orange', 'grapes', 'strawberry'

    ],

    'Computer-parts':

    ['keyboard', 'mouse', 'monitor', 'cpu', 'usb', 'hard drive']

}

print("Your categories are: ", ' | '.join(category))

def check(categorya, q):

    c = 0

    picked = []

    picked1 = []

    for k, v in category.items():

        if k == categorya:

            #r=k.lower()

            picked.extend(v)

            for p in picked:

                if q in p:

                    picked1.append(p)

                    c += 1

    if c == 0:

        q = input(

            "No items has the letter you entered. Please enter a different letter "

        )

        checklist(categorya, temp_Var=q)

    else:

        print(

            "\nThere are {0} out of {1} items in my list that has this letter".

            format(c, len(picked)))

    count = 0

    while True:

        answer = input("\nGuesed the item? What do you think it is? ")

        if not answer:

            input("\nDo you want to quit the game? Press Enter to quit")

            break

        if answer in picked1:

            design()

            print("\nHey smarty pants! You figured it out :-)\n")

            design()

            #break

            time.sleep(1)

            eq = input("Do you want to quit? [Y/N] ")

            if eq.lower() == 'y':

                sys.exit("Thank you for playing! :-)")

            else:

                print("\nAlright. Let's keep playing")

                catelist()

        else:

            if count == 0:

                q1 = input("\nNah. Would you like some clues? ")

                picked_first = []

                picked_last = []

                t = 0

                t1 = 0

                if q1.lower() == 'yes':

                    for p in picked1:

                        if q == p[0]:

                            t = 1

                            picked_first.append(p)

                        elif q == p[-1]:

                            t1 = 1

                            picked_last.append(p)

                    if t == True:

                        print(

                            "\nThe letter you entered is the first letter of one/some of the items"

                        )

                    elif t1 == True:

                        print(

                            "\nThe letter you entered is the last letter of one/some of the items"

                        )

                    else:

                        print(

                            "\nThe entered letter is not the first or last letter of the item. It's in the {} position of the item".

                            format(p.find(q) + 1))

            elif count > 0 and count < 2:

                print(

                    "\nOkay. I will reveal some of the letters of the item. It starts with {0} and ends with {1}{2}".

                    format(p[0], p[-2], p[-1]))

            elif count > 1 and count < 3:

                s = list(p)

                random.shuffle(s)

                shuffledr = ''.join(s)

                print(

                    "\nTough nut to crack? \nAlright. Last clue. I am going to show you a gibberish version of the word. Try to assemble the letters properly to find the item\n\n\t\t{}".

                    format(shuffledr))

            else:

                print("\nSorry. No more clues")

        count += 1

def catelist():

    while True:

        categoryq = input(

            "\nWhich category you choose? [Press Enter to quit the game] ")

        if not categoryq:

            input("\nDo you want to quit the game? Press 'ANY' key ")

            sys.exit("\nThank you for playing! :-)")

        categorya = categoryq[0].upper() + categoryq[1:].lower()

        if categorya not in category.keys():

            print("Please check the spellings")

            catelist()

        checklist(categorya)

def checklist(categorya, temp_Var=None):

    if temp_Var == None:

        q = input("Enter a letter: (Should be one letter and only letter) ")

        checklist2(categorya, q)

    else:

        checklist2(categorya, temp_Var)

def checklist2(categorya, inputvar):

    if inputvar.isdigit():

        inputvar = input("Please enter a letter, not a number ")

        #if q.isdigit()==False:

        #checklist(q,categorya)

        if len(inputvar) > 1:

            inputvar = input("Please enter a letter: ")

    if inputvar.isdigit() or len(inputvar) > 1:

        checklist(categorya)

    if inputvar.isdigit() == False and len(inputvar) == 1:

        check(categorya, inputvar)

catelist()

