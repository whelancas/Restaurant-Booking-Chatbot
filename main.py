import nameManagement
from util import checkForExit

def main():

    username = "User"

    print("Hello! If you wish to exit at any point, type EXIT. What is your name?")
    userInput = checkForExit(username)
    username = userInput

    print(f"Hi, {username}.")

    while True:
        print("How can I help you?")
        userInput = checkForExit(username)




if __name__ == "__main__":
    main()   