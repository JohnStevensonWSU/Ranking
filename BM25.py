import IndexList
import csv
import math

class BM25(object):
    def __init__(self, dataFile):
        self.dataFile = dataFile
        self.index = self.index(dataFile)

    # Creates an index over the corpus given
    # as a CSV dataFile.
    def index(self, dataFile):
        index = IndexList.indexList()

        file = open(dataFile)
        reader = csv.reader(file, delimiter=",")
        docID = 0
        terms = 0

        for line in reader:
            if docID == 0:
                print("Columns: " + line[0] + ", " + line[1])
            else:
                terms += len(line[1].split(" "))
                for term in line[1].split(" "):
                    index.add(term, int(line[0]))
            print(docID)
            docID += 1

        index.print()
        self.docNum = docID - 1 
        print(self.docNum)
        self.avgDocLength = terms / self.docNum
        return index

    def bm25(self, query, k):
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
                    scores.append(self.query(doc,query))

        results = list(zip(docIDs, scores))
        results.sort(key = lambda x: x[1], reverse=True)
        print(len(results))

        for result in results:
            if count >= k:
                break
            count += 1
            print(result)

    def query(self, docID, query):
        N = self.docNum
        k1 = 1.2
        k2 = 500
        b = 0.75
        d = self.termCount(docID)
        terms = query.split(" ")
        termUnq = []
        result = 0
        avgd = self.avgDocLength
        print(docID)

        for term in terms:
            if term not in termUnq:
                termUnq.append(term)

        for term in termUnq:
            dft = self.index.getDocNumber(term)
            print(dft)
            qft = 0
            for t in terms:
                if t == term:
                    qft += 1
            
            ft = self.index.termFreq(term, docID)
            one = math.log((N - dft + 0.5) / (dft + 0.5)) 
            two = ((k1 + 1) * ft)/(((k1 * (1 - b)) + (b * d / avgd)) + ft) 
            print(two)
            print("k1: " + str(k1))
            print("ft: " + str(ft))
            print("b: " + str(b))
            print("d: " + str(d))
            print("avgd: " + str(avgd))
            three = ((k2 + 1) * qft) / (k2 + qft)
            result += one * two * three

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


bm25 = BM25("wine.csv")

while True:
    query = input("What would you like to search for? ")
    k = int(input("How many search results would you like? "))
    bm25.bm25(query, k)
