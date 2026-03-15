from flask import Flask, render_template
from flask_socketio import SocketIO
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app, cors_allowed_origins="*")

client = MongoClient("mongodb://localhost:27017/")
db = client["chat_app"]

from sockets.chat_socket import register_socket_events
register_socket_events(socketio, db)

@app.route("/")
def index():
    return render_template("chat.html")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)