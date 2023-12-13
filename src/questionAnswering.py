from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = []
answers = []

with open("data/qa-dataset.csv", 'r', encoding='utf8') as file:
        for line in file:
            columns = line.lower().strip('\n').strip('?').split(',')
            questions.append(columns[0])
            answers.append(columns[1])

def qaSimilarity(userInput):
    tdfidfVectoriser = TfidfVectorizer()
    tdidfMatrix = tdfidfVectoriser.fit_transform(questions + [userInput.strip('?').lower()])

    cosine = cosine_similarity(tdidfMatrix[-1], tdidfMatrix[:-1])

    mostSimilarIndex = cosine.argmax() # returns index of highest value in matrix
    probability = cosine.max() # rteurns highest probability (num between 0 and 1)
    mostSimilarQ = questions[mostSimilarIndex]
    mostSimilarA = answers[mostSimilarIndex]

    if probability > 0.55: 
        return [mostSimilarQ, mostSimilarA]
    else:
         return False