

## 🛡️ Phishing URL Detection API

An **AI-powered phishing detection system** that identifies whether a URL is malicious or legitimate using machine learning. The system is built with **Python**, powered by a **Random Forest model**, and exposed via a **REST API using Flask**. It is fully **Dockerized** and deployed on **Render Cloud** for real-time public access.

> 🔒 Designed for real-world application security, machine learning deployment, and REST API development experience.

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Docker](https://img.shields.io/badge/Dockerized-Yes-brightgreen)
![ML Model](https://img.shields.io/badge/ML-RandomForest-orange)
![Deployment](https://img.shields.io/badge/Render-Deployed-blue)
![Status](https://img.shields.io/badge/API-Live-green)

---

## 📌 Project Summary

This project demonstrates the complete **end-to-end pipeline** of a machine learning system in production:

* ✅ Data preprocessing
* ✅ Feature engineering from URLs
* ✅ Supervised model training
* ✅ Model serialization
* ✅ REST API development
* ✅ Docker containerization
* ✅ Cloud deployment using Render

---

## 🚀 Features

* 🔍 Real-time phishing detection via URL analysis
* 📦 RESTful API built using **Flask**
* 🤖 Model trained on over **27,000 URLs** (phishing + legitimate)
* 🧠 Uses **RandomForestClassifier** from Scikit-learn
* 🐳 Packaged in a **Docker container**
* ☁️ Publicly deployed using **Render.com**

---

## 📦 Technologies Used

| Layer          | Tech Stack                            |
| -------------- | ------------------------------------- |
| Backend API    | Flask + Flask-CORS                    |
| ML Model       | Scikit-learn (RandomForestClassifier) |
| Language       | Python 3.10                           |
| Model Training | Pandas, NumPy, Joblib                 |
| Packaging      | Docker                                |
| Deployment     | Render (Docker Web Service)           |
| Versioning     | Git + GitHub                          |

---

## 📁 Project Structure

```bash
phishing-detector/
├── app.py                # Flask API server
├── train_model.py        # ML training script (runs in Docker)
├── feature_extractor.py  # Feature engineering from URL strings
├── cleaned_data.csv      # Dataset (URLs + labels)
├── phishing_model.pkl    # Trained model (auto-generated in Docker)
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker build config
└── README.md             # Project documentation
```

---

## 🧠 How It Works

1. **Input:** A raw URL like `http://paypal-login-secure.com`
2. **Feature Extraction:**

   * Length of URL
   * Count of `@`, `.`, `-`, `//`, and `https`
   * Presence of suspicious keywords like `login`, `verify`, `secure`
3. **Model Prediction:**

   * Trained Random Forest model predicts:

     * `Phishing` (1)
     * `Legitimate` (0)
4. **Output:** Returns prediction as JSON via REST API

---

## 🧪 API Endpoints

### 🔗 `/` (GET)

**Health Check**

```json
{
  "message": "Phishing URL Detection API is running ✅"
}
```

---

### 🔐 `/predict` (POST)

**Send a URL to be classified**

#### Request

```json
{
  "url": "http://secure-paypal-login.com"
}
```

#### Response

```json
{
  "url": "http://secure-paypal-login.com",
  "result": "Phishing"
}
```

---

## 🧪 Try it Live (Cloud Hosted on Render)

> 🌐 Public URL (Deployed via Docker on Render)

```
https://phishing-detector.onrender.com/
```

Test with:

```bash
curl -X POST https://phishing-detector.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"http://secure-login-paypal.com\"}"
```

---

## 🐳 Local Development with Docker

### 📥 1. Clone the Repo

```bash
git clone https://github.com/Dipanshu6265/Phishing-detector.git
cd Phishing-detector
```

### 🛠 2. Build the Docker Image

```bash
docker build -t phishing-detector .
```

### ▶️ 3. Run the Container

```bash
docker run -p 5000:5000 phishing-detector
```

### 🔍 4. Test Locally

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"http://example-login.com\"}"
```

---

## 🧠 Model Training Details

* **Model Type:** Random Forest Classifier
* **Accuracy:** \~95% on hold-out test data
* **Training:** Automatically triggered inside Docker via `train_model.py`
* **Dataset:** [Kaggle: Phishing URL Dataset](https://www.kaggle.com/datasets/sid321axn/phishing-site-url)

---

## 👨‍💻 Author

**Dipanshu**

* GitHub: [@Dipanshu6265](https://github.com/Dipanshu6265)
* LinkedIn: *[(https://www.linkedin.com/feed/?nis=true&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BXL3eNWLKSkeFA1%2BwCgjYHw%3D%3D)]*
---

## 📄 License

This project is licensed under the MIT License.

---

