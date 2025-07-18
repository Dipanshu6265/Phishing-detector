from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("phishing_model.pkl")

@app.route('/')
def home():
    return jsonify({"message": "Phishing URL Detection API is running ✅"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Sample feature extraction (simplified)
    features = [
        len(url),
        url.count('.'),
        url.count('@'),
        url.count('-'),
        url.count('//'),
        int('https' in url),
        int('login' in url.lower())
    ]

    prediction = model.predict([features])[0]

    return jsonify({
        "url": url,
        "result": "Phishing" if prediction == 1 else "Legitimate"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
