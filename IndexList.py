import IndexNode

# indexList is a linked list representing a term index
# for a document corpus. 
class indexList(object):

    # Constructor creates an indexList whose 
    # head points to an indexNode for the 
    # given term. 
    def __init__(self):
        self.head = None

    # Adds a term/docID tuple to the indexList
    def add(self, term, docID):
        # Find the node that either corresponds
        # with the given term or is right before
        # where the term should go in the index.
        node = self.search(self.head, term)

        # Add term to the beginning of the index 
        if node is None:
            self.head = IndexNode.indexNode(term, docID, None)
            return

        # Replace head of list 
        if node == -1:
            self.head = IndexNode.indexNode(term, docID, self.head)
            return

        # Add term to existing indexNode
        if node.term == term:
            node.add(term, docID)
            return

        nextTemp = node.nextIndexNode
        node.nextIndexNode = IndexNode.indexNode(term, docID, nextTemp)
        return

    # Searches for indexNode whose term is the 
    # given term. It returns either the indexNode
    # whose term is the given term or the node 
    # whose term is just before the given term
    # alphabetically.
    def search(self, indexNode, term):
        # Create a node pointer.
        node = indexNode

        # Return None if the list is empty.
        if node is None:
            return node

        # While there is node after the current node,
        while node.nextIndexNode is not None:
            # Return current node if it has the search term.
            if node.term == term:
                return node
            # Return current node if the next node's term comes 
            # after the search term in the alphabet.
            elif node.nextIndexNode.term > term:
                return node
            node= node.nextIndexNode

        return node

    # Prints the index list who calls the method
    def print(self):
        indexNode = self.head
        count = 0
        while indexNode is not None:
            count += 1
            print(indexNode.term)
            docNode = indexNode.docList.head
            while docNode is not None:
                print("(" + str(docNode.docID) + "," + str(docNode.freq) + ")")
                docNode = docNode.nextDocNode
            indexNode = indexNode.nextIndexNode

    # Returns the DocList associated with a term.
    # If no term exists in the index, returns None.
    def getIndexNode(self, term):
        indexNode = self.search(self.head, term)

        if indexNode is None:
            return None
        elif indexNode == -1:
            return None
        elif indexNode.term != term:
            return None

        return indexNode

    def termFreq(self, term, docID):
        node = self.search(self.head, term)
        
        if node is None:
            return 0
        elif node == -1:
            return 0
        elif node.term != term:
           return 0
        
        return node.docList.getFreq(docID)

    def getDocNumber(self, term):
        node = self.search(self.head, term)
        
        if node is None:
            return 0
        elif node == -1:
            return 0
        elif node.term != term:
            return 1

        return node.docList.count()
    
    def getDocs(self, term):
        node = self.search(self.head, term)

        if node is None:
            return None
        elif node == -1:
            return None
        elif node.term != term:
            return None

        return node.docList.getDocs()


