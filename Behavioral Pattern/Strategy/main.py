# Chiến lược đi lại
class Strategy:
    def travel(self):
        pass

class BusStrategy(Strategy):
    def travel(self):
        print("Đi làm bằng xe bus")

class BikeStrategy(Strategy):
    def travel(self):
        print("Đi làm bằng xe máy")

class WalkStrategy(Strategy):
    def travel(self):
        print("Đi bộ đi làm")

# Context
class Person:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def go_to_work(self):
        self.strategy.travel()

# Demo
Person(BusStrategy()).go_to_work()
Person(BikeStrategy()).go_to_work()
Person(WalkStrategy()).go_to_work()
