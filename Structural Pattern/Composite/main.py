class File:
    def show(self): print("Tệp")

class Folder:
    def __init__(self): self.children = []
    def add(self, item): self.children.append(item)
    def show(self):
        for child in self.children: child.show()

folder = Folder()
folder.add(File())
folder.add(File())
folder.show()
