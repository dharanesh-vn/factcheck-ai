from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import sys
import os

# -----------------------------
# Path setup for src/
# -----------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

# -----------------------------
# Model import
# -----------------------------
try:
    from predict import predict_news
except Exception as e:
    print("Model import failed:", e)
    def predict_news(text):
        return "ERROR"

# -----------------------------
# Flask app
# -----------------------------
application = Flask(__name__)

# ✅ UNIVERSAL CORS SETUP (ROBUST)
# This handles the preflight OPTIONS requests and injects headers into all responses.
CORS(application, resources={r"/*": {"origins": "*"}})

@application.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# -----------------------------
# Routes
# -----------------------------
@application.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "FactCheck AI API is active"
    })

@application.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    # Handle preflight manually as a backup
    if request.method == 'OPTIONS':
        return make_response('', 200)

    try:
        data = request.get_json(force=True)

        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data['text']
        result = predict_news(text)

        return jsonify({
            "prediction": result,
            "is_real": result == "REAL"
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# -----------------------------
# Local run (ignored in EB)
# -----------------------------
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)