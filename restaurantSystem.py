from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from util import checkForExit

discoverability = """
        What I can do:
        1. Make a booking
        2. Alter a booking
        3. Cancel a booking
        4. Find information on a restaurant
            (e.g. opening times, address, contact info, etc.)
"""

queries = []
responses = []

with open("discoverability.csv", 'r', encoding='utf8') as file:
    for line in file:
        columns = line.lower().strip('\n').strip('?').split(',')
        queries.append(columns[0])
        responses.append(columns[1])

def discoverabilitySimilarity(userInput):
    tfidfVectoriser = TfidfVectorizer()
    tdidfMatrix = tfidfVectoriser.fit_transform(queries + [userInput.strip('?').lower()])

    cosine = cosine_similarity(tdidfMatrix[-1], tdidfMatrix[:-1])

    mostSimilarIndex = cosine.argmax()
    probability = cosine.max()
    mostSimilarQ = queries[mostSimilarIndex]
    mostSimilarR = responses[mostSimilarIndex]

    if probability > 0.55 or userInput in ["1", "2", "3", "4"]: 
        if mostSimilarR == "1" or userInput == "1":
            ret = bookingReservation()
        elif mostSimilarR == "1" or userInput == "2":
            ret = editingReservation()
        elif mostSimilarR == "1" or userInput == "3":
            ret = cancellingReservation()
        elif mostSimilarR == "1" or userInput == "4":
            ret = restaurantInfo()
        else:
            return [mostSimilarQ, discoverability]
        
        return [mostSimilarQ, ret]
    
    return False

def bookingReservation():
    print("\n\nMaking a Reservation\n")

    print("To go back, type BACK.\n")
    userInput = checkForExit()
    if userInput.lower() == "back":
        return

    print(userInput)

def editingReservation():
    return "Editing"

def cancellingReservation():
    return "Cancelling"

restaurants = []
with open("restaurants.csv", 'r', encoding='utf8') as file:
    for line in file:
        restaurants.append(line.strip("\n").split(","))

def restaurantInfo():
    print("\nHere are the restaurants you can make reservations at:")
    for res in restaurants:
        print(f"""
              {res[0]}
              Opening Hours: {res[1]}
              Alternative Menus: {res[2]}
              Address: {res[3]}
              Phone Number: {res[4]}
              Email: {res[5]}
                """)


