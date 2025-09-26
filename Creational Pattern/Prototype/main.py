import copy

class Document:
    def __init__(self, content):
        self.content = content

    def clone(self):
        return copy.deepcopy(self)


# Demo
doc1 = Document("Original File")
doc2 = doc1.clone()
doc2.content = "Cloned File"

print(doc1.content)  # Original File
print(doc2.content)  # Cloned File
