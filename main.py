import IndexList

def main():
    index = IndexList.indexList()

    index.add("hello", 1)
    index.add("hello", 1)
    index.add("hello", 1)
    index.add("hello", 2)
    index.add("hello", 2)
    index.add("hello", 3)
    
    index.add("there", 1)
    index.add("there", 1)
    index.add("there", 2)
    index.add("there", 2)
    index.add("there", 3)
    
    index.add("how", 3)
    
    index.add("are", 3)

    index.add("you", 3)

    index.add("a", 3)

    indexNode = index.head

    while indexNode is not None:
        print(indexNode.term)
        docNode = indexNode.docList.head
        while docNode is not None:
            print("(" + str(docNode.docID) + "," + str(docNode.freq) + ")")
            docNode = docNode.nextDocNode
        indexNode = indexNode.nextIndexNode

    return
    print("Term: " + indexNode.term)
    print("Document: " + str(docID))
    print("Frequency: " + str(freq))

main()

