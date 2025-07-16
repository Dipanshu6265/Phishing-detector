import pandas as pd
from feature_extractor import extract_features
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

print("📦 Starting model training...")

# Confirm dataset exists
if not os.path.exists("cleaned_data.csv"):
    raise FileNotFoundError("❌ cleaned_data.csv not found in Docker image")

df = pd.read_csv("cleaned_data.csv")

# Extract features from URLs
X = df['url'].apply(extract_features).tolist()
y = df['label']

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
acc = accuracy_score(y_test, clf.predict(X_test))
print(f"✅ Training complete with accuracy: {acc:.4f}")

# Save model
joblib.dump(clf, "phishing_model.pkl")
print("✅ Model saved as phishing_model.pkl")
