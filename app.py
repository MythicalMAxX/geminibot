from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

API_key = "YOUR-API-KEY"
MODEL_NAME = "gemini-1.5-flash"

genai.configure(api_key=API_key)

app = Flask(__name__)

#gemini-vision-pro

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/api/generate", methods=["POST"])
def generate_api():
    req_body = request.get_json()
    content = req_body.get('contents')
#     history = """
# User: hii how are you doing today?

# Bot: The provided translation is already excellent. There's no need for improvement. नमस्ते! आज आप कैसे हैं? (Namaste! Aaj aap kaise hain?) is a perfectly natural and appropriate translation of "Hi, how are you doing today?".
# """
    model = genai.GenerativeModel(model_name=MODEL_NAME)
    # response = model.generate_content(f"You are a translator and your job is to translate english to hindi. Now translate this content: {content} answer with referenc to our chat history {history}")
    response = model.generate_content(content)
    response_text = "".join(chunk.text for chunk in response)
    print(response_text)
    return jsonify({"text":response_text})


if __name__ == "__main__":
    app.run(debug=True)