from flask_socketio import emit, join_room
from datetime import datetime

def register_socket_events(socketio, db):

    @socketio.on("join_room")
    def handle_join(data):
        room = data.get("room")
        join_room(room)
        emit("message", {"msg": f"User joined {room}"}, room=room)

    @socketio.on("send_message")
    def handle_message(data):
        message = {
            "user": data.get("user"),
            "room": data.get("room"),
            "text": data.get("text"),
            "timestamp": datetime.utcnow()
        }

        db.messages.insert_one(message)
        emit("message", message, room=data.get("room"))