class RealImage:
    def display(self): print("Hiển thị ảnh")

class ProxyImage:
    def __init__(self): self.real = None
    def display(self):
        if self.real is None: self.real = RealImage()
        self.real.display()

img = ProxyImage()
img.display()
