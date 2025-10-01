class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler
    
    def handle(self, request):
        if self.next:
            return self.next.handle(request)

class Leader(Handler):
    def handle(self, request):
        if request <= 2:  # nghỉ <= 2 ngày
            print("Leader duyệt nghỉ", request, "ngày")
        else:
            super().handle(request)

class Manager(Handler):
    def handle(self, request):
        if request <= 5:  # nghỉ <= 5 ngày
            print("Manager duyệt nghỉ", request, "ngày")
        else:
            super().handle(request)

class Director(Handler):
    def handle(self, request):
        print("Director duyệt nghỉ", request, "ngày")

# Tạo chuỗi: Leader -> Manager -> Director
chain = Leader(Manager(Director()))

# Demo
chain.handle(1)  # Leader duyệt
chain.handle(4)  # Manager duyệt
chain.handle(7)  # Director duyệt
