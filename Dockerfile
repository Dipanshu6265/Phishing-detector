FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Train the model (this must succeed to generate phishing_model.pkl)
RUN python train_model.py

EXPOSE 5000

CMD ["python", "app.py"]
