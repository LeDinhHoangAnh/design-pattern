class Burger:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        return "Burger with " + ", ".join(self.parts)


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bread(self): self.burger.add("bread"); return self
    def add_meat(self): self.burger.add("meat"); return self
    def add_veggies(self): self.burger.add("veggies"); return self

    def build(self): return self.burger


# Demo
builder = BurgerBuilder()
burger = builder.add_bread().add_meat().add_veggies().build()
print(burger.show())   # Burger with bread, meat, veggies
