
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyD5zsEXypFFQ2mCCHBGWnnY0Mnu8LPf69o")

model = genai.GenerativeModel(
    "gemini-1.5-pro",
    system_instruction="You are a supportive mental health assistant named Siri. Always reply in a short, kind, and easy-to-understand way."
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/siri")
def siri_chat():
    return render_template("siri.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"response": "Please enter a message so I can help you."})

    try:
        prompt = f"Reply in a short, simple, and comforting way: {user_input}"
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception:
        return jsonify({"response": "Oops! Something went wrong. Please try again later."})

if __name__ == "__main__":
    app.run(debug=True)
