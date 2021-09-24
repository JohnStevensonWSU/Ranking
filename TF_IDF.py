import IndexList
import csv

class TF_IDF(object):
    """TF-IDF Class"""
    
    # Constructor for TF_IDF class
    def __init__(self, dataFile):
        # Make index over terms in the corpus
        self.index = self.index(dataFile)

    # Creates an index over the corpus given
    # as a CSV dataFile.
    def index(self, dataFile):
        index = IndexList.indexList()

        file = open(dataFile)
        reader = csv.reader(file, delimiter=",")
        docID = 0
        count = 0

        for line in reader:
            print(docID)
            if docID > 70:
                break
            if docID == 0:
                print("Columns: " + line[0] + ", " + line[1])
            else:
                for term in line[1].split(" "):
                    count += 1
                    index.add(term, docID)
            docID += 1
        index.print()

tf_idf = TF_IDF("wine.csv")
