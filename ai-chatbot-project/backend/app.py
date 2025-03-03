import logging
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from routes.chat import chat_bp
from routes.kakao import kakao_bp
from routes.naver import naver_bp
from routes.telegram import telegram_bp

# ✅ 로그 설정 추가
logging.basicConfig(level=logging.DEBUG)  # ✅ DEBUG까지 출력 설정
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})  # 모든 출처 허용

# ✅ API 라우트 등록
app.register_blueprint(chat_bp)
app.register_blueprint(kakao_bp)
app.register_blueprint(naver_bp)
app.register_blueprint(telegram_bp)

@app.route("/")  # 루트 경로 추가
def home():
    logger.info("✅ 홈 페이지 요청이 들어옴!")
    return jsonify({"message": "Flask 서버 정상 작동 중!"})

if __name__ == "__main__":
    logger.info("🚀 Flask 서버 시작됨 (PORT: 5001)")
    app.run(host="0.0.0.0", port=5000, debug=False)
