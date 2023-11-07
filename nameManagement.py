from util import checkForExit

def giveName(input, username):
    if "my" in input.lower() and "name" in input.lower():
        print(f"Your name is {username}")

    elif "your" in input.lower() and "name" in input.lower():
        print("I do not have a name.")

def changeName(input, username):
    if "change" in input.lower() and "name" in input.lower():
        print("What would you like to change your name to?")
        newName = checkForExit(username)
        print(f"Hello, {newName}.")
        
        return newName
    
    return False