from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("phishing_model.pkl")

# Health check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Phishing URL Detection API is running ✅"})

# ✅ Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url", "")

    # Feature extraction
    features = [
        len(url),
        url.count("."),
        url.count("@"),
        int("https" in url),
        int("login" in url)
    ]

    prediction = model.predict([features])[0]
    result = "Phishing" if prediction == 1 else "Legitimate"

    return jsonify({
        "url": url,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
