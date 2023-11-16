from util import checkForExit
from nameManagement import *
from intentMatching import stDiscClassifier
from questionAnswering import qaSimilarity

def mainLoop(username):
    while True:
        userInput = checkForExit(username)

        ### NAME MANAGEMENT ###
        giveUsername = giveName(userInput, username)
        if giveUsername != False:
            mainLoop(username)

        changeUsername = changeName(userInput, username)
        if changeUsername != False:
            username = changeUsername
            mainLoop(username)

        ### QUESTION ANSWERING ###

        question = qaSimilarity(userInput)
        print(question)

        ### INITIAL INTENT MATCHING ###
        initialIntent = stDiscClassifier(userInput)
        
        if initialIntent[0] == "unclear":
            print("I don't understand, sorry. Please could you rephrase?")
        elif initialIntent[0] == "confirm":
            if initialIntent[1] == "small talk":
                print("maybe small talk")
            else:
                print("maybe discoverability")
        elif initialIntent[0] == "small talk":
            print("small talk")
        else:
            print("discoverability")

def main():

    username = "User"

    print("\n\nHello! If you wish to exit at any point, type EXIT. What is your name?")
    userInput = checkForExit(username)
    username = userInput

    print(f"Hi, {username}.")

    mainLoop(username)


if __name__ == "__main__":
    main()   