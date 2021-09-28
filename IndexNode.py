import DocList

# indexNode is a node in a linked list representing a 
# term index for a document corpus.
class indexNode(object):
    # Constructor creates indexNode for given term.
    # nextIndexNode given is the nextIndexNode of the 
    # created indexNode. docList is initialized to 
    def __init__(self, term, docID, nextIndexNode):
        self.term = term
        self.docList = DocList.docList(docID)
        self.nextIndexNode = nextIndexNode

    # Adds a term/docID tuple to docList of an indexNode
    def add(self, term, docID):
        self.docList.add(docID)
        
    # Prints the Index Node that calls the method.
    def print(self):
        print(self.term)
        self.docList.print()
