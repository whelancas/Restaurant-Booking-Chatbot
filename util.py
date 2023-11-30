def checkForExit(username):
    userTag = username + ": "
    userInput = input(userTag)

    if userInput.lower() == "exit":
        print("Okay, goodbye!")
        exit()

    return userInput
