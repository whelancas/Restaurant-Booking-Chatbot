import time

def checkForExit(username):
    userTag = username + ": "
    userInput = input(userTag)

    if userInput.lower() == "back":
        print("Bot: Returning...")
        time.sleep(1)

    if userInput.lower() == "exit":
        print("Bot: Okay, goodbye!")
        exit()

    return userInput
