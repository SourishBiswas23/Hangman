import random
from os import system
import hangmanStages
import hangmanWords


def createBlankList():
    blankList = []
    for i in range(8):
        blankList.append('-')
    return blankList


def changeList(blankList, guess):
    change = False
    for index in range(len(chosenWord)):
        if guess == chosenWord[index]:
            blankList[index] = guess
            change = True
    return change


chosenWord = random.choice(hangmanWords.words)
blankList = createBlankList()
lives = 6
system("clear")
while lives > 0:
    guess = input("Enter a letter: ").lower()
    change = changeList(blankList, guess)
    if not change:
        lives -= 1
    else:
        if '-' not in blankList:
            print("You Have Won The Game")
            exit(0)

    system("clear")
    print(hangmanStages.stages[6-lives])
    print(blankList)

print(f"Chosen Word: {chosenWord}")
