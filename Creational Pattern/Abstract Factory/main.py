class Chair:
    def sit(self): pass

class ModernChair(Chair):
    def sit(self): return "Sitting on a modern chair"

class ClassicChair(Chair):
    def sit(self): return "Sitting on a classic chair"


class FurnitureFactory:
    def create_chair(self): pass

class ModernFactory(FurnitureFactory):
    def create_chair(self): return ModernChair()

class ClassicFactory(FurnitureFactory):
    def create_chair(self): return ClassicChair()


# Demo
factory = ModernFactory()     # chọn style hiện đại
chair = factory.create_chair()
print(chair.sit())            # Sitting on a modern chair
