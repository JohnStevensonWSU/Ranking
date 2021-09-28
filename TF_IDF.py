import IndexList
import csv
import math

class TF_IDF(object):
    """TF-IDF Class"""
    
    # Constructor for TF_IDF class
    def __init__(self, dataFile):
        # Make index over terms in the corpus
        self.index = self.index(dataFile)
        self.dataFile = dataFile

    # Creates an index over the corpus given
    # as a CSV dataFile.
    def index(self, dataFile):
        index = IndexList.indexList()

        file = open(dataFile)
        reader = csv.reader(file, delimiter=",")
        docID = 0
        count = 0

        for line in reader:
            if count > 100:
                break
            if count == 0:
                print("Columns: " + line[0] + ", " + line[1])
            else:
                for term in line[1].split(" "):
                    index.add(term, int(line[0]))
            print(count)
            count += 1
        index.print()
        print(docID)
        return index
    
    # Performs a query on the corpus and returns the top k results.
    # Each result is returned with a document id and a TF-IDF score.
    def tfidf(self, query, k):
        terms = query.split(" ")
        docIDs = []
        scores = []
        results = []
        count = 0

        for term in terms:
            docs = self.index.getDocs(term)
            for doc in docs:
                if doc not in docIDs:
                    docIDs.append(doc)
                    scores.append(self.relevance(doc,query))

        results = list(zip(docIDs,scores))
        results.sort(key = lambda x: x[1], reverse=True)

        for result in results:
            if count >= k:
                break
            count += 1
            print(result)
        
    def relevance(self, d, query):
        terms = query.split(" ")
        relevance = 0
        tf = 0

        print(terms)
        for term in terms:
            tf = self.tf(d, term)
            docNum = self.index.getDocNumber(term)
            relevance += self.tf(d, term) / self.index.getDocNumber(term)

        return relevance

    def tf(self, d, t):
        termCount = self.termCount(d)
        termFreq = self.index.termFreq(t, d)
        print(termFreq)
        result = math.log(1 + termFreq / termCount)
        return result

    def termCount(self, d):
        file = open(self.dataFile)
        reader = csv.reader(file, delimiter=",")
        count = 0
        docID = -1
        doc = None

        for line in reader:
            if docID == d:
                doc = line[1]
                break
            docID += 1
        try:
            return len(doc.split(" ")) - 1
        except:
            return 0

tf_idf = TF_IDF("wine.csv")
while True:
    query = input("What would you like to search for? ")
    k = int(input("How many search results would you like? "))
    tf_idf.tfidf(query, k)
