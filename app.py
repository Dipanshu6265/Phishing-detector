from flask import Flask, request, jsonify
import joblib
from feature_extractor import extract_features
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow requests from frontend (if you build one)

# Load the trained model
model = joblib.load('phishing_model.pkl')

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Phishing URL Detection API is running ✅"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        url = data.get("url", "")
        if not url:
            return jsonify({"error": "Missing URL in request"}), 400

        features = extract_features(url)
        prediction = model.predict([features])[0]
        result = "Phishing" if prediction == 1 else "Legitimate"

        return jsonify({
            "url": url,
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
