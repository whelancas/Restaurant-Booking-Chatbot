from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

from nltk.corpus import stopwords

### INITIAL INTENT MATCHING ###

docs = {
    "small talk":       "smalltalk.csv",
    "discoverability":  "discoverability.csv",
    "qa":               "qa-dataset.csv"
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

xTrain, xTest, yTrain, yTest = train_test_split(data, labels, stratify=labels, test_size=0.25, random_state=1)

countVect = CountVectorizer(stop_words=stopwords.words('english'))
xTrainCounts = countVect.fit_transform(xTrain)
tfidTransformer = TfidfTransformer(use_idf=True, sublinear_tf=True).fit(xTrainCounts)
xTrainTF = tfidTransformer.transform(xTrainCounts)

classifier = LogisticRegression(random_state=0).fit(xTrainTF, yTrain)

### EVALUATION ###

xTestCounts = countVect.transform(xTest)
xTestTfidf = tfidTransformer.transform(xTestCounts)

predicted = classifier.predict(xTestTfidf)

print(confusion_matrix(yTest, predicted))
print(accuracy_score(yTest, predicted))

testInput = ['how are you today?', 'can you help me book a table?', 'hello']
# expected output: small talk, discoverability, small talk

processedTestInput = countVect.transform(i.strip('?').lower() for i in testInput)
processedTestInput = tfidTransformer.transform(processedTestInput)

print(classifier.predict(processedTestInput))