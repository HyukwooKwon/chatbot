from flask import Blueprint, request, jsonify
from chatbot import get_chatbot_response

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        bot_reply = get_chatbot_response(user_message)
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": "서버 오류 발생"}), 500
