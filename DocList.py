import DocNode

# docList is a linked list that represents a term
# frequency list for a term.
class docList(object):
    
    # Constructor creates a docList whose 
    # head points to a newly-created docNode.
    # This docNode is created with given docID.
    def __init__(self, docID):
        self.head = DocNode.docNode(docID, None)
    
    def add(self, docID):
        # Find the node that either corresponds 
        # with the given docID or the end of the 
        # list. 
        node = self.search(self.head, docID)

        # Create a docNode for the given docID.
        if node is None:
            node = DocNode.docNode(docID, None)
            return
        
        # Increase the frequency for the docNode
        if node.docID == docID:
            node.incrFreq()
            return

        node.nextDocNode = DocNode.docNode(docID, None)
        return         

    # Search for a docNode with the given docID
    def search(self, docNode, docID):
        node = docNode

        # Return node if docList is empty.
        if node is None:
            return node

        # While another node exists beyond the current one,
        while node.nextDocNode is not None:
            # Return the current node if it matches the docID
            if node.docID == docID:
                return node
            node = node.nextDocNode

        return node

    # Prints the Doc List that calls the method.
    def print(self):
        node = self.head

        while node is not None:
            node.print()
            node = node.nextDocNode

        return

    # Returns the frequency of a term in a document.
    def getFreq(self, docID):
        node = self.head

        while node is not None:
            if node.docID == docID:
                return node.freq
            node = node.nextDocNode

        # If the docID does not exist, return 1
        return 0

    def count(self):
        node = self.head
        count = 0

        while node is not None:
            count+= 1
            node = node.nextDocNode

        return count

    def getDocs(self):
        node = self.head
        docs = []

        while node is not None:
            docs.append(node.docID)
            node = node.nextDocNode

        return docs
