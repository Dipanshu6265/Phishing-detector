import joblib
from feature_extractor import extract_features

model = joblib.load('phishing_model.pkl')

test_url = "http://secure-update-paypal.com/login"
features = extract_features(test_url)

prediction = model.predict([features])[0]
print("Prediction:", "Phishing" if prediction else "Legitimate")
