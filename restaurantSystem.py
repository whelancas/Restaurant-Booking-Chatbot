from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

    if probability > 0.55: 
        if mostSimilarR == "1":
            ret = bookingReservation()
        elif mostSimilarR == "2":
            ret = editingReservation()
        elif mostSimilarR == "3":
            ret = cancellingReservation()
        elif mostSimilarR == "4":
            ret = restaurantInfo()
        else:
            return [mostSimilarQ, discoverability]
        
        return [mostSimilarQ, ret]
    
    return False

def bookingReservation():
    return "Booking"

def editingReservation():
    return "Editing"

def cancellingReservation():
    return "Cancelling"

def restaurantInfo():
    return "Info"


### TESTING ###

