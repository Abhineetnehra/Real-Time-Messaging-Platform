class Message:
    def __init__(self, user, room, text, timestamp):
        self.user = user
        self.room = room
        self.text = text
        self.timestamp = timestamp