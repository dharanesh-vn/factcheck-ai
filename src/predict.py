import joblib
import os

# Absolute safe path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, '..', 'model', 'model.pkl')
vectorizer_path = os.path.join(BASE_DIR, '..', 'model', 'vectorizer.pkl')

# Load once (IMPORTANT)
model = None
vectorizer = None

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print("✅ Model loaded successfully")
except Exception as e:
    print("❌ Error loading model:", str(e))


def predict_news(text):
    if model is None or vectorizer is None:
        return "MODEL_ERROR"

    try:
        # SIMPLE CLEAN (NO NLTK)
        text = text.lower()

        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]

        return "REAL" if pred == 1 else "FAKE"

    except Exception as e:
        print("Prediction error:", str(e))
        return "ERROR"