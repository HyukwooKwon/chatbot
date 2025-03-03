from flask import Flask, render_template, request, jsonify, Blueprint  # render_template 추가
from flask_cors import CORS
from routes.chat import chat_bp
from routes.kakao import kakao_bp
from routes.naver import naver_bp
from routes.telegram import telegram_bp

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})  # 모든 출처 허용

# ✅ API 라우트 등록
app.register_blueprint(chat_bp)
app.register_blueprint(kakao_bp)
app.register_blueprint(naver_bp)
app.register_blueprint(telegram_bp)

@app.route("/")  # 루트 경로 추가
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)