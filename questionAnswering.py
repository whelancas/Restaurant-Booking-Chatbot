from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = []
answers = []

with open("qa-dataset.csv", 'r', encoding='utf8') as file:
        for line in file:
            columns = line.lower().strip('\n').strip('?').split(',')
            questions.append(columns[0])
            answers.append(columns[1])

def qaSimilarity(userInput):
      tfidfVectoriser = TfidfVectorizer()
      tdidfMatrix = tfidfVectoriser.fit_transform(questions + [userInput.strip('?').lower()])

      cosine = cosine_similarity(tdidfMatrix[-1], tdidfMatrix[:-1])

      print(cosine)

      mostSimilarIndex = cosine.argmax()
      mostSimilarQ = questions[mostSimilarIndex]
      mostSimilarA = answers[mostSimilarIndex]

      return [mostSimilarQ, mostSimilarA]