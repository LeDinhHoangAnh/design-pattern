class State:
    def handle(self):
        pass

class OpenState(State):
    def handle(self):
        print("Cửa đang mở")

class ClosedState(State):
    def handle(self):
        print("Cửa đang đóng")

class Door:
    def __init__(self, state):
        self.state = state
    
    def set_state(self, state):
        self.state = state
    
    def press_button(self):
        self.state.handle()

# Demo
door = Door(OpenState())
door.press_button()

door.set_state(ClosedState())
door.press_button()
