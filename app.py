from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("phishing_model.pkl")

# Health check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Phishing URL Detection API is running ✅"})

# ✅ THIS IS WHAT MUST EXIST:
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data["url"]

    # Example dummy features
    features = [
        len(url),                     # URL length
        url.count("."),              # Dots in URL
        url.count("@"),              # @ symbol
        "https" in url,              # HTTPS used
        "login" in url               # Keyword check
    ]
    # Predict
    prediction = model.predict([features])[0]

    return jsonify({
        "url": url,
        "result": "Phishing" if prediction == 1 else "Legitimate"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
