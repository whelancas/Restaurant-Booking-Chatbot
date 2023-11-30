from util import checkForExit
from nameManagement import *
from intentMatching import stDiscClassifier, smalltalkSimilarity
from questionAnswering import qaSimilarity

discoverability = """
        What I can do:
        1. Make a booking
        2. Alter a booking
        3. Cancel a booking
        4. Find information on a restaurant
            (e.g. opening times, address, contact info, etc.)
"""

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
        if question != False:
            print(f"The answer to '{question[0]}' is: {question[1]}")
            mainLoop(username)

        ### INITIAL INTENT MATCHING ###
        initialIntent = stDiscClassifier(userInput)
        smalltalk = smalltalkSimilarity(userInput)
        
        if initialIntent[0] == "unclear":
            print("I don't understand, sorry. Please could you rephrase?")
        elif initialIntent[0] == "confirm":
            if initialIntent[1] == "small talk":
                if smalltalk != False:
                    print(smalltalk[1])
                else:
                    print("I don't understand, sorry. Please could you rephrase?")
            else:
                print(discoverability)
        elif initialIntent[0] == "small talk":
            if smalltalk != False:
                print(smalltalk[1])
            else:
                print("I don't understand, sorry. Please could you rephrase?")
        else:
            print(discoverability)

def main():

    username = "User"

    print("\n\nHello! If you wish to exit at any point, type EXIT. What is your name?")
    userInput = checkForExit(username)
    username = userInput

    print(f"Hi, {username}.")

    mainLoop(username)


if __name__ == "__main__":
    main()   