from flask import Blueprint, request, jsonify
from chatbot import get_chatbot_response
from config import KAKAO_REST_API_KEY

kakao_bp = Blueprint("kakao", __name__)

@kakao_bp.route("/chat/kakao", methods=["POST"])
def kakao_chat():
    try:
        data = request.json
        user_message = data.get("userRequest", {}).get("utterance", "")

        bot_reply = get_chatbot_response(user_message)

        return jsonify({
            "version": "2.0",
            "template": {
                "outputs": [{"simpleText": {"text": bot_reply}}]
            }
        })

    except Exception as e:
        return jsonify({"error": "서버 오류 발생"}), 500
