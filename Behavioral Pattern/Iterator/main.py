class MyIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.collection)
    
    def next(self):
        item = self.collection[self.index]
        self.index += 1
        return item

# Demo
songs = ["Bài 1", "Bài 2", "Bài 3"]
it = MyIterator(songs)

while it.has_next():
    print("Đang phát:", it.next())
