import joblib
import os
import sys
from preprocessing import clean_text

model_path = os.path.join(os.path.dirname(__file__), '../model/model.pkl')
vectorizer_path = os.path.join(os.path.dirname(__file__), '../model/vectorizer.pkl')

if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    print("Model or Vectorizer not found. Please run train.py first.")
    model = None
    vectorizer = None
else:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

def predict_news(text):
    if model is None or vectorizer is None:
        return "Model not trained"
    text = clean_text(text)
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    return "REAL" if pred == 1 else "FAKE"
