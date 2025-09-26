def add_cheese(pizza_func):
    def wrapper(): return pizza_func() + " + Cheese"
    return wrapper

@add_cheese
def make_pizza(): return "Pizza"

print(make_pizza())  # Pizza + Cheese
