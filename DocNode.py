# docNode class represents a node in a linked list.
# A Node has fields docID, frequency, and nextDocNode. 
class docNode(object):
    """docNode object represents a node in linked list of documents for TF-IDF"""

    # Constructor creates a node for term.
    # Field nextDocNode is set to existing 
    # docNode.
    def __init__(self, docID, nextDocNode):
        self.docID = docID
        self.freq = 1
        self.nextDocNode = nextDocNode

    # Increases the frequency of the docNode
    # frequency.
    def incrFreq(self):
        self.freq += 1
