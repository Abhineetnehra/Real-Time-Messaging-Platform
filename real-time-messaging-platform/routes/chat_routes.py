from flask import Blueprint

chat_routes = Blueprint("chat_routes", __name__)

@chat_routes.route("/chat")
def chat():
    return "Chat route placeholder"