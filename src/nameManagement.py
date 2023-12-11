from util import checkForExit

def giveName(input, username):
    if "my" in input.lower() and "name" in input.lower() and "change" not in input.lower():
        print(f"Bot: Your name is {username}")

    elif "your" in input.lower() and "name" in input.lower():
        print("Bot: I do not have a name.")

    else:
        return False

def changeName(input, username):
    if "change" in input.lower() and "name" in input.lower():
        print("Bot: What would you like to change your name to?")
        newName = checkForExit(username)
        print(f"Bot: Hello, {newName}.")
        
        return newName
    
    else:
        return False