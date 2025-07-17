from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
from feature_extractor import extract_features

app = Flask(__name__)
CORS(app)

model = joblib.load('phishing_model.pkl')

@app.route('/')
def index():
    return jsonify({'message': 'Phishing URL Detection API is running ✅'})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'url' not in data:
        return jsonify({'error': 'Missing "url" in request'}), 400

    url = data['url']
    features = extract_features(url)
    prediction = model.predict([features])[0]

    # 🎯 New: Add confidence score from predict_proba
    proba = model.predict_proba([features])[0]
    confidence = round(max(proba) * 100, 2)

    result = 'Phishing' if prediction == 1 else 'Legitimate'
    return jsonify({
        'url': url,
        'result': result,
        'confidence': f"{confidence}%"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
