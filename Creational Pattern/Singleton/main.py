class President:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(President, cls).__new__(cls)
            cls._instance.name = "The Only President"
        return cls._instance


# Demo
p1 = President()
p2 = President()

print(p1.name)   # The Only President
print(p1 is p2)  # True -> cả hai cùng trỏ về một đối tượng duy nhất
