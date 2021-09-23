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
    def search(self, node, docID):
        # Return node if docList is empty.
        if node is None:
            return node

        # Return node if it is the node that 
        # corresponds with the given docID.
        if node.docID == docID:
            return node

        # Return current docNode if you've
        # reached the last node.
        if node.nextDocNode is None:
            return node

        return self.search(node.nextDocNode, docID)

        

