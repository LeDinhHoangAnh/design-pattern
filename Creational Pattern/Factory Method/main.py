class Coffee:
    def serve(self):
        pass

class Espresso(Coffee):
    def serve(self):
        return "Serving Espresso"

class Latte(Coffee):
    def serve(self):
        return "Serving Latte"

class CoffeeFactory:
    @staticmethod
    def create_coffee(type_):
        if type_ == "espresso":
            return Espresso()
        elif type_ == "latte":
            return Latte()
        else:
            raise ValueError("Unknown coffee type")


# Demo
coffee1 = CoffeeFactory.create_coffee("espresso")
coffee2 = CoffeeFactory.create_coffee("latte")

print(coffee1.serve())  # Serving Espresso
print(coffee2.serve())  # Serving Latte
