class Command:
    def execute(self):
        pass

class TurnOnTV(Command):
    def execute(self):
        print("TV được bật")

class TurnOffTV(Command):
    def execute(self):
        print("TV được tắt")

class RemoteControl:
    def __init__(self, command):
        self.command = command
    
    def press_button(self):
        self.command.execute()

# Demo
RemoteControl(TurnOnTV()).press_button()
RemoteControl(TurnOffTV()).press_button()
