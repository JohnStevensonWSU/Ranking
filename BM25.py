import IndexList
import csv
import math
import time

# BM25 is a class that allows you to perform
# queries on a corpus using the BM25 algorithm.
# The constructor takes a csv datafile of docIDs
# and documents and creates an inverted index
# over the corpus. 
class BM25(object):
    def __init__(self, dataFile):
        self.dataFile = dataFile
        self.index = self.index(dataFile)

    # Creates an index over the corpus given
    # as a CSV dataFile.
    def index(self, dataFile):
        # Initialize an empty index.
        index = IndexList.indexList()

        # Open the dataFile given to the constructor.
        file = open(dataFile)
        reader = csv.reader(file, delimiter=",")
        docID = 0
        terms = 0

        # Create the index over the corpus by adding every 
        # unique word to the index.
        for line in reader:
            if docID == 0:
                print("Columns: " + line[0] + ", " + line[1])
            else:
                terms += len(line[1].split(" "))
                for term in line[1].split(" "):
                    index.add(term, int(line[0]))
            docID += 1

        index.print()
        self.docNum = docID - 1 
        print("Processed " + str(self.docNum) + " documents and " + str(terms) + " terms.")
        self.avgDocLength = terms / self.docNum
        return index

    # Performs the BM25 algorithm on the given query.
    # Prints out the top k results. 
    def bm25(self, query, k):
        # Split the query into terms
        terms = query.split(" ")
        docIDs = []
        scores = []
        results = []
        count = 0

        # Search for documents that contain the terms
        # in the query. 
        for term in terms:
            docs = self.index.getDocs(term)
            for doc in docs:
                if doc not in docIDs:
                    docIDs.append(doc)
                    # Get the BM25 score for the document
                    scores.append(self.query(doc,query))

        # Create a list of tuples containing the DocIDs and
        # their scores.
        results = list(zip(docIDs, scores))
        results.sort(key = lambda x: x[1], reverse=True)

        # Print out the top k results.
        for result in results:
            if count >= k:
                break
            count += 1
            print(result)

    # Query calculates the BM25 score for a 
    # given docID on the given query. 
    def query(self, docID, query):
        # Get all variables that are independent of 
        # the search term.
        N = self.docNum
        k1 = 1.2
        k2 = 500
        b = 0.75
        d = self.termCount(docID)
        terms = query.split(" ")
        termUnq = []
        result = 0
        avgd = self.avgDocLength

        for term in terms:
            if term not in termUnq:
                termUnq.append(term)

        for term in terms:
            # Get all variables that are dependent on
            # the search term. 
            dft = self.index.getDocNumber(term)
            print(dft)
            qft = 0
            for t in terms:
                if t == term:
                    qft += 1
            ft = self.index.termFreq(term, docID)
            # Calculate the parts of the BM25 equation
            one = math.log((N - dft + 0.5) / (dft + 0.5)) 
            two = ((k1 + 1) * ft)/(((k1 * (1 - b)) + (b * d / avgd)) + ft) 
            three = ((k2 + 1) * qft) / (k2 + qft)
            # Add all term scores together.
            result += one * two * three

        return result
            
    # Calculates the number of terms in a given document.
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

start = time.time()
bm25 = BM25("wine.csv")
end = time.time()
runtime = end - start
print("Index took " + str(runtime) + " to initialize.")

while True:
    query = input("What would you like to search for? ")
    k = int(input("How many search results would you like? "))
    bm25.bm25(query, k)
