import random, time, datetime

then = datetime.datetime.now()

print("Welcome to the game of Guessing. The time now is ", then)

fruits = ["Apple", "Banana", "Strawberry", "Papaya", "Grapes", "Orange"]

print(

    "The list of fruits are: \n{0}\n and you have 3 seconds to guess the fruit".

    format(fruits))

time.sleep(3)

while True:

    i = input("Guessed the fruit? Please enter here")

    if not i: break

    if i == random.choice(fruits):

        print("Hey! You guessed it right!")

        now = datetime.datetime.now()

        print("The time now is ", now)

        print("The amount of time you took to win this game is ", now - then)

        break

    else:

        print("But the computer thought the fruit ", random.choice(fruits))

