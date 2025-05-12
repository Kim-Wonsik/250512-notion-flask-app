from flask import Flask, jsonify
import json

# Flask 앱 생성
app = Flask(__name__)

# JSON 파일 경로 설정
JSON_FILE = "notion_data.json"

# 📌 라우트 설정: /data로 접속하면 JSON 데이터를 반환합니다.
@app.route('/data', methods=['GET'])
def get_data():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "JSON 파일을 찾을 수 없습니다."}), 404

# 📌 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
