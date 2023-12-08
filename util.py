import time

setUsername = "User"

def checkForExit(username=setUsername):
    global setUsername
    setUsername = username

    userTag = username + ": "
    userInput = input(userTag)

    if userInput.lower() == "back":
        print("Returning...")
        time.sleep(1)

    if userInput.lower() == "exit":
        print("Okay, goodbye!")
        exit()

    return userInput
