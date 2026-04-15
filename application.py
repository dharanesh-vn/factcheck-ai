from flask import Flask, request, jsonify
import joblib
import os
import sys

# Set up paths
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)

from predict import predict_news

application = Flask(__name__)

@application.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "FactCheck AI Cloud Service",
        "deployment": "AWS Elastic Beanstalk"
    })

@application.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    result = predict_news(data['text'])
    return jsonify({
        "prediction": result,
        "is_real": result == "REAL"
    })

if __name__ == "__main__":
    # AWS Elastic Beanstalk expects the app to run on port 5000 by default if not specified
    application.run(host='0.0.0.0', port=5000)
