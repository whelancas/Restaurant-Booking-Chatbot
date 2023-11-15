from util import checkForExit
from nameManagement import *

def main():

    username = "User"

    print("Hello! If you wish to exit at any point, type EXIT. What is your name?")
    userInput = checkForExit(username)
    username = userInput

    print(f"Hi, {username}.")

    while True:
        print("User: ")
        userInput = checkForExit(username)

        ### NAME MANAGEMENT ###
        giveName(userInput)
        changeName = changeName(userInput, username)
        if changeName != False:
            username = changeName

        ### INITIAL INTENT MATCHING ###


        




if __name__ == "__main__":
    main()   