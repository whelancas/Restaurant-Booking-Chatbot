from util import checkForExit
from nameManagement import *
from intentMatching import stDiscClassifier, smalltalkSimilarity
from questionAnswering import qaSimilarity
from restaurantSystem import discoverabilitySimilarity

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
        disc = discoverabilitySimilarity(userInput)

        if initialIntent[0] == "confirm":
            if initialIntent[1] == "small talk" and smalltalk != False:
                print(f"I think you said {smalltalk[0]}, so...")
                print(smalltalk[1])
            elif initialIntent[1] == "discoverability" and disc != False:
                if disc[1] == False:
                    print(f"I think you said {disc[0]}, so...")
                    print(discoverability)
                else:
                    print(disc[1])

        elif initialIntent[0] == "small talk" and smalltalk != False:
            print(smalltalk[1])

        elif initialIntent[0] == "discoverability" and disc != False:
            if disc[1] == False:
                print(discoverability)
            else:
                print(disc[1])
        
        else:
            print("I don't understand, sorry. Please could you rephrase?")



def main():

    username = "User"

    print("\n\nHello! If you wish to exit at any point, type EXIT. What is your name?")
    userInput = checkForExit(username)
    username = userInput

    print(f"Hi, {username}.")

    mainLoop(username)


if __name__ == "__main__":
    main()   