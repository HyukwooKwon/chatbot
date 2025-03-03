import openai
import logging
from config import OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_chatbot_response(user_message):
    try:
        logger.info(f"🔹 사용자 메시지: {user_message}")  # ✅ 사용자 입력 로그 추가

        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=100,
            temperature=0.5
        )

        bot_response = response.choices[0].message.content.strip()
        logger.info(f"💬 챗봇 응답: {bot_response}")  # ✅ 챗봇 응답 로그 추가

        return bot_response

    except Exception as e:
        logger.error(f"❌ Chatbot Error: {str(e)}")
        return "서버 오류 발생"
