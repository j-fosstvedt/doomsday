import datetime
import random

maxDelta = 160

def newDate():
    today = datetime.datetime.today()
    delta = datetime.timedelta(days=random.randrange(365 * -maxDelta, 365 * maxDelta))
    today += delta
    return today



def askPlayer():
    guessDate = newDate()
    if guessDate.isoweekday() == 7:
        guessWeekday = 0
    else:
        guessWeekday = guessDate.isoweekday()
    guess = input(str(guessDate.strftime("%d %B %Y")) + ": ")
    if int(guess) == guessWeekday:
        print("Correct :)")
    else:
        print("Noob :(")
        print(guessWeekday)

while True:
    try:
        askPlayer()
    except:
        print("You did something wrong, hopefully")
    continueGame = input("Continue? (Y/n) ")
    if continueGame == "y" or continueGame == "Y" or continueGame == "":
        continue
    elif continueGame == "n" or continueGame == "N":
        break
    else:
        print("That's gibberish, so we'll continue")
        continue