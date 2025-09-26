class Color:
    def apply(self): pass
class Red(Color):
    def apply(self): return "Đỏ"
class Blue(Color):
    def apply(self): return "Xanh"

class Shape:
    def __init__(self, color): self.color = color
class Circle(Shape):
    def draw(self): print("Vẽ hình tròn màu", self.color.apply())

circle = Circle(Red())
circle.draw()
