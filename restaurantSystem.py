from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from util import checkForExit

### BRANCHING ###

queries = []
responses = []

with open("discoverability.csv", 'r', encoding='utf8') as discFile:
    for line in discFile:
        columns = line.lower().strip('\n').strip('?').split(',')
        queries.append(columns[0])
        responses.append(columns[1])

def discoverabilitySimilarity(userInput, username):
    tfidfVectoriser = TfidfVectorizer()
    tdidfMatrix = tfidfVectoriser.fit_transform(queries + [userInput.strip('?').lower()])

    cosine = cosine_similarity(tdidfMatrix[-1], tdidfMatrix[:-1])

    mostSimilarIndex = cosine.argmax()
    probability = cosine.max()
    mostSimilarQ = queries[mostSimilarIndex]
    mostSimilarR = responses[mostSimilarIndex]

    if probability > 0.55 or userInput in ["1", "2", "3", "4"]: 
        if mostSimilarR == "1" or userInput == "1":
            ret = bookingReservation(username)
        elif mostSimilarR == "2" or userInput == "2":
            ret = editingReservation(username)
        elif mostSimilarR == "3" or userInput == "3":
            ret = cancellingReservation(username)
        elif mostSimilarR == "4" or userInput == "4":
            ret = restaurantInfo()
        else:
            return [mostSimilarQ, False]
        
        return [mostSimilarQ, ret]
    
    return [False]

### COLLECTED INFO ###

reservation = {
    "name": "",
    "restaurant": "",
    "date": "",
    "time": "",
    "group size": ""
}

### RESERVATION BOOKING ###       
        
def bookingReservation(username):
    print("\n\nMaking a Reservation\n")
    print("Bot: To go back, type BACK.\n")

    for field in reservation:
        while reservation[field] == "":
            print(f"Bot: What {field} is the booking for?")
            userInput = checkForExit(username)
            if userInput.lower() == "back":
                return "\n"
                        
            print(f"Bot: Please confirm that the {field} is {userInput} (yes/no)")
            confirmInput = checkForExit(username)
            if confirmInput.lower() == "back":
                return "\n"
                    
            if "y" in confirmInput.lower():
                reservation[field] = userInput 

    print("\n\nFinal confirmation\n")
    for field in reservation:
        print(f"{field}: {reservation[field]}")
    print("\nBot: Is this correct (yes/no)?")

    confirmInput = checkForExit(username)
    if confirmInput.lower() == "back":
        return "\n"
    
    if "y" in confirmInput.lower():
        reference = f"{reservation['name']}{reservation['group size']}"
        with open("bookings.csv", 'a', encoding='utf8') as bookingsFile:
            bookingsFile.write(f"{reservation['name']},{reservation['restaurant']},{reservation['date']},{reservation['time']},{reservation['group size']},{reference}\n")

        print(f"Bot: Your reservation has been made. Your reference code is {reference}.")

    elif "n" in confirmInput.lower():
        editingReservation(username)

    return "\n"


### RESERVATION EDITING ###

def editingReservation(username):
    print("\n\nEditing a Reservation\n")
    print("Bot: To go back, type BACK.\n")

    print("Bot: Please enter your booking reference code.")
    userInput = checkForExit(username)
    if userInput.lower() == "back":
        return "\n"
    
    with open("bookings.csv", 'r', encoding='utf8') as bookingsFile:
        for line in bookingsFile:
            entry = line.split(',')
            if entry[5] == userInput:
                reservation["name"] = entry[0]
                reservation["restaurant"] = entry[1]
                reservation["date"] = entry[2]
                reservation["time"] = entry[3]
                reservation["group size"] = entry[4]
    
    for field in reservation:
        print(f"{field}: {reservation[field]}")


### RESERVATION CANCELLING ###
    
def cancellingReservation(username):
    print("\n\nCancel a Reservation\n")
    print("Bot: To go back, type BACK.\n")

    userInput = checkForExit(username)
    if userInput.lower() == "back":
        return "\n"
    


### RESTAURANT INFO ###

restaurants = []
with open("restaurants.csv", 'r', encoding='utf8') as restFile:
    for line in restFile:
        restaurants.append(line.strip("\n").split(","))

def restaurantInfo():
    print("\nBot: Here are the restaurants you can make reservations at:")
    for res in restaurants:
        print(f"""
              {res[0]}
              Opening Hours: {res[1]}
              Alternative Menus: {res[2]}
              Address: {res[3]}
              Phone Number: {res[4]}
              Email: {res[5]}
                """)
    
    return "\n"


