class YouTubeChannel:
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, user):
        self.subscribers.append(user)
    
    def notify(self, video):
        for sub in self.subscribers:
            sub.update(video)

class User:
    def __init__(self, name):
        self.name = name
    
    def update(self, video):
        print(f"{self.name} nhận thông báo: Video mới - {video}")

# Demo
channel = YouTubeChannel()
channel.subscribe(User("An"))
channel.subscribe(User("Bình"))

channel.notify("Python dễ hiểu trong 10 phút")
