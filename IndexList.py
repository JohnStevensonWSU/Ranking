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
        # Return None if the indexList is empty.
        if indexNode is None:
            return indexNode

        # Return -1 if the head needs to be replaced.
        if indexNode.term > term:
            return -1

        # Return current indexNode if the next
        # node is None.
        if indexNode.nextIndexNode is None:
            return indexNode

        # Return the indexNode if it's term is 
        # the given term.
        if indexNode.term == term:
            return indexNode

        # Return the indexNode if the next term
        # is after the given term alphabetically.
        if indexNode.nextIndexNode.term > term:
            return indexNode

        # Search with the next indexNode and return 
        # its output.
        return self.search(indexNode.nextIndexNode, term)

    def print(self):
        indexNode = self.head
        count = 0

        while indexNode is not None:
            count += 1
            print(count)
            print(indexNode.term)
            docNode = indexNode.docList.head
            while docNode is not None:
                print("(" + str(docNode.docID) + "," + str(docNode.freq) + ")")
                docNode = docNode.nextDocNode
            indexNode = indexNode.nextIndexNode
