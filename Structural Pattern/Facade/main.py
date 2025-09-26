class Lights: 
    def on(self): print("Đèn bật")
class TV: 
    def on(self): print("TV bật")

class HomeFacade:
    def __init__(self): self.tv, self.lights = TV(), Lights()
    def start_movie(self):
        self.lights.on()
        self.tv.on()

home = HomeFacade()
home.start_movie()
