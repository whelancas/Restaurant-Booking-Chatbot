from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances

from nltk.corpus import stopwords

### INITIAL INTENT MATCHING ###

docs = {
    "small talk":       "smalltalk.csv",
    "discoverability":  "discoverability.csv",
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

countVect = CountVectorizer(stop_words=stopwords.words('english'))
xTrainCounts = countVect.fit_transform(xTrain)
tfidTransformer = TfidfTransformer(use_idf=True, sublinear_tf=True).fit(xTrainCounts)
xTrainTF = tfidTransformer.transform(xTrainCounts)

classifier = LogisticRegression(random_state=0).fit(xTrainTF, yTrain)

### COSINE SIMILARITY ###



### EVALUATION ###

xTestCounts = countVect.transform(xTest)
xTestTfidf = tfidTransformer.transform(xTestCounts)

predicted = classifier.predict(xTestTfidf)

#print(confusion_matrix(yTest, predicted))
#print(accuracy_score(yTest, predicted))

testInput = ['was you day nice', 'can you help me book a table?', 'can i reserve a table at blue dragon']
# expected output: small talk, discoverability, discoverability

processedTestInput = countVect.transform(i.strip('?').lower() for i in testInput)
processedTestInput = tfidTransformer.transform(processedTestInput)

#print(classifier.predict(processedTestInput))

def stDiscClassifier(query):
    processedInput = countVect.transform([query.strip('?').lower()])
    processedInput = tfidTransformer.transform(processedInput)

    return(classifier.predict(processedInput))
