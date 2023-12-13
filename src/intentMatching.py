from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

### SMALL TALK COSINE SIMILARITY ###

questions = []
answers = []

with open("data/smalltalk.csv", 'r', encoding='utf8') as file:
    for line in file:
        columns = line.lower().strip('\n').strip('?').split(',')
        questions.append(columns[0])
        answers.append(columns[1])

def smalltalkSimilarity(userInput):
    # Finds the best match to the user input in the samll talk dataset
    tfidfVectoriser = TfidfVectorizer()
    tdidfMatrix = tfidfVectoriser.fit_transform(questions + [userInput.strip('?').lower()])

    cosine = cosine_similarity(tdidfMatrix[-1], tdidfMatrix[:-1])

    mostSimilarIndex = cosine.argmax()
    probability = cosine.max()
    mostSimilarQ = questions[mostSimilarIndex]
    mostSimilarA = answers[mostSimilarIndex]

    if probability > 0.55: 
        return [mostSimilarQ, mostSimilarA]
    
    return [False]


### INITIAL INTENT MATCHING CLASSIFIER ###

docs = {
    "small talk":       "data/smalltalk.csv",
    "discoverability":  "data/discoverability.csv",
}

data = []
labels = []

for doc in docs.keys():
    with open(docs[doc], 'r', encoding='utf8') as file:
        for line in file:
            columns = line.lower().strip('\n').strip('?').split(',')
            data.append(columns[0])
            labels.append(doc)

#print(data)
#print(labels)

xTrain, yTrain = data, labels
#xTrain, yTrain, xTest, yTest = train_test_split(data, labels, train_size=0.25, random_state=1)

countVect = CountVectorizer()
xTrainCounts = countVect.fit_transform(xTrain)
tfidfTransformer = TfidfTransformer(use_idf=True, sublinear_tf=True).fit(xTrainCounts)
xTrainTF = tfidfTransformer.transform(xTrainCounts)

classifier = LogisticRegression(random_state=0).fit(xTrainTF, yTrain)

### EVALUATION ###

"""
xTestCounts = countVect.transform(xTest)
xTestTfidf = tfidTransformer.transform(xTestCounts)

predicted = classifier.predict(xTestTfidf)
print(classifier.predict_proba(xTestTfidf))

print(xTestTfidf)

print(confusion_matrix(yTest, predicted))
print(accuracy_score(yTest, predicted))

testInput = ['was you day nice', 'can you help me book a table?', 'can i reserve a table at blue dragon']
 expected output: small talk, discoverability, discoverability

processedTestInput = countVect.transform(i.strip('?').lower() for i in testInput)
processedTestInput = tfidTransformer.transform(processedTestInput)

print(classifier.predict(processedTestInput))
print(classifier.predict_proba(processedTestInput))
"""

def stDiscClassifier(query):
    # Classifies an input as either small talk or discovery

    minThreshold = 0.53
    confidentTheshold = 0.65

    processedInput = countVect.transform(i.strip('?').lower() for i in [query])
    processedInput = tfidfTransformer.transform(processedInput)

    probability = classifier.predict_proba(processedInput)
    
    if probability.max() < minThreshold and (query not in ["1", "2", "3", "4"]):
        return ["unclear"]
    elif probability.max() > minThreshold and probability.max() < confidentTheshold:
        return ["confirm", classifier.predict(processedInput)]
    else:
        return(classifier.predict(processedInput))

    
