from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_response   # 👈 Import your python function

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]

    reply = get_response(user_message)   # 👈 Call your function

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)