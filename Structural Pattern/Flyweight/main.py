class TreeType:
    def __init__(self, name): self.name = name
_tree_cache = {}

def get_tree(name):
    if name not in _tree_cache:
        _tree_cache[name] = TreeType(name)
    return _tree_cache[name]

t1 = get_tree("Oak")
t2 = get_tree("Oak")
print(t1 is t2)  # True
