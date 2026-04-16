# FactCheck AI: Enterprise Cloud Platform

## 1. System Overview
FactCheck AI is a centralized Machine Learning as a Service (MLaaS) platform for misinformation detection. It utilizes a Passive Aggressive Classifier (PAC) to analyze linguistic patterns in news content.

## 2. Global Architecture
The project supports two independent production-grade deployment strategies.

### **Option A: Distributed AWS Stack (Primary)**
- **Role**: High-performance decoupled architecture.
- **Frontend**: Amazon S3.
- **Backend API**: AWS Elastic Beanstalk (EC2).
- **CDN**: Amazon CloudFront.

### **Option B: Standalone Analytical Dashboard (Alternative)**
- **Role**: Isolated, unified verification platform.
- **Service**: Streamlit Community Cloud.
- **Inference**: Local model execution (Zero AWS dependency).

---

## 3. Standalone Deployment Guide (Streamlit Cloud)
Follow these steps to deploy the dashboard as an independent entity:

### **Phase 1: Repository Preparation**
- Ensure all model artifacts are present in the `/model` directory.
- Verify `requirements.txt` contains `streamlit`, `scikit-learn`, `joblib`, and `pandas`.
- Confirm `app/app.py` is configured for **Standalone Mode** (local import of `predict.py`).

### **Phase 2: Cloud Configuration**
1.  Initialize a repository on GitHub and push the latest project volume.
2.  Navigate to [share.streamlit.io](https://share.streamlit.io).
3.  Authenticate using GitHub credentials.
4.  Select **"New app"** and point to your repository.
5.  **Critical Configuration**:
    - **Main file path**: `app/app.py`
    - **Python version**: 3.10+
6.  Click **"Deploy"**. The system will automatically build the environment and launch the analytics interface.

---

## 4. Technical Registry
- **Structure**:
    - `/app`: Analytical Dashboard source.
    - `/model`: Trained AI model artifacts.
    - `/src`: Inference engine and processing logic.
    - `application.py`: Master API source.
- **Registry**:
    - Dhanushya E (2303717673722009)
    - Dharanesh VN (2303717673721010)
    - Coursework: 22MDC65
    - Staff: Dr. Savithri V, Dr. Chandia S, Dr. Kamatchi A

## 5. Active Production URLS
- **Distributed Interface (S3)**: https://factcheck-ui-unique-name.s3.us-east-1.amazonaws.com/index.html
- **Analytical API (CloudFront)**: https://dyzfcyb8dw1ce.cloudfront.net/predict
- **Standalone Dashboard**: [Your Streamlit URL here]
