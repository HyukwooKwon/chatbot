from flask import Blueprint, request, jsonify
from chatbot import get_chatbot_response
import logging

naver_bp = Blueprint("naver", __name__)
logger = logging.getLogger(__name__)

@naver_bp.route("/chat/naver", methods=["POST"])
def naver_talktalk():
    try:
        data = request.json
        user_message = data.get("text", "")

        if not user_message:
            return jsonify({"event": "send", "text": "메시지를 입력해주세요."})

        bot_reply = get_chatbot_response(user_message)
        logger.info(f"네이버 톡톡 | 사용자: {user_message} | 챗봇: {bot_reply}")

        # 네이버 톡톡 API 응답 형식
        return jsonify({
            "event": "send",
            "text": bot_reply
        })

    except Exception as e:
        logger.error(f"네이버 톡톡 Webhook 오류: {str(e)}")
        return jsonify({"error": "서버 오류 발생"}), 500
