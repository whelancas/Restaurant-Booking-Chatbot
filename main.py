from util import checkForExit
from nameManagement import *
from intentMatching import stDiscClassifier

def main():

    username = "User"

    print("\n\nHello! If you wish to exit at any point, type EXIT. What is your name?")
    userInput = checkForExit(username)
    username = userInput

    print(f"Hi, {username}.")

    while True:
        userInput = checkForExit(username)

        ### NAME MANAGEMENT ###
        giveName(userInput, username)
        changeUsername = changeName(userInput, username)
        if changeUsername != False:
            username = changeUsername

        ### INITIAL INTENT MATCHING ###
        print(stDiscClassifier(userInput))

        




if __name__ == "__main__":
    main()   