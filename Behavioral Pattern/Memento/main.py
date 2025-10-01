# Memento lưu trạng thái
class Memento:
    def __init__(self, state):
        self.state = state

# Đối tượng có thể tạo/lấy lại trạng thái
class TextEditor:
    def __init__(self):
        self.text = ""
    
    def write(self, words):
        self.text += words
    
    def save(self):
        return Memento(self.text)
    
    def restore(self, memento):
        self.text = memento.state

# Caretaker quản lý lịch sử
class History:
    def __init__(self):
        self.history = []
    
    def push(self, memento):
        self.history.append(memento)
    
    def pop(self):
        return self.history.pop()

# Demo
editor = TextEditor()
history = History()

editor.write("Xin chào. ")
history.push(editor.save())   # lưu trạng thái

editor.write("Hôm nay học Python. ")
history.push(editor.save())   # lưu tiếp

print("Trước khi Undo:", editor.text)

# Undo 1 lần
editor.restore(history.pop())
print("Sau khi Undo:", editor.text)

# Undo thêm 1 lần
editor.restore(history.pop())
print("Sau khi Undo lần 2:", editor.text)
