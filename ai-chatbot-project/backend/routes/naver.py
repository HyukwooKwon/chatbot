from flask import Blueprint, request, jsonify
from chatbot import get_chatbot_response

naver_bp = Blueprint("naver", __name__)

@naver_bp.route("/chat/naver", methods=["POST"])
def naver_talktalk():
    try:
        data = request.json
        user_message = data.get("text", "")

        bot_reply = get_chatbot_response(user_message)

        return jsonify({"event": "send", "text": bot_reply})

    except Exception as e:
        return jsonify({"error": "서버 오류 발생"}), 500
