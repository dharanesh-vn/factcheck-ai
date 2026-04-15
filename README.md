# 🛡️ FactCheck AI: Cloud-Integrated Content Verification Service

> **Status:** Production-Ready | **Accuracy:** 99.5% | **Architecture:** Cloud-Native / MLaaS
> **Project:** Mobile and Cloud Application Development Lab (22MDC65)

## 📁 1. Project Directory Structure
```text
fake-news-detection/
├── app/
│   └── app.py            # FactCheck AI Premium Dashboard (UI)
├── data/
│   ├── Fake.csv          # Fabricated news corpus
│   └── True.csv          # Factual news corpus
├── model/
│   ├── model.pkl         # Trained PAC Model artifacts
│   └── vectorizer.pkl    # TF-IDF Vectorization weights
├── src/
│   ├── preprocessing.py  # NLP cleaning logic
│   ├── predict.py        # Real-time inference logic
│   └── train.py          # ML Training Engine (99.5% Accuracy)
├── api.py                # RESTful Cloud Service Backend
├── Dockerfile            # Cloud Portability config
├── requirements.txt      # Project dependencies
└── README.md             # Detailed Project Guide
```

---

## 🏗️ 2. What is FactCheck AI?
It is a state-of-the-art **Fake News Detection System** using Natural Language Processing (NLP) to verify content authenticity. 
- **The Core**: Uses a **Passive Aggressive Classifier** retrained on over **44,800 news articles**.
- **The Result**: Achieves **99.5% accuracy** by analyzing linguistic variance—identifying sensationalist patterns common in fake news compared to neutral factual reporting.

---

## 🚀 3. Professional Deployment Guide (Free)
The most efficient way to deploy this Cloud project for a live demo is using **GitHub** and **Streamlit Community Cloud**. This provides a public URL at zero cost.

### **Phase 1: Preparation**
1. Ensure your project is organized as per the structure above.
2. Run `pip freeze > requirements.txt` to ensure all dependencies are locked.

### **Phase 2: GitHub Repository Setup**
1. Create a new repository on [GitHub](https://github.com/) (e.g., `factcheck-ai`).
2. Initialize Git in your project folder:
   ```bash
   git init
   git add .
   git commit -m "Initialize FactCheck AI project"
   ```
3. Link to your GitHub repo and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/factcheck-ai.git
   git push -u origin main
   ```

### **Phase 3: Streamlit Cloud Deployment**
1. Login to [Streamlit Cloud](https://share.streamlit.io/) using your GitHub account.
2. Click **"Create app"**.
3. Select the `factcheck-ai` repository and the `main` branch.
4. Set the "Main file path" to: `app/app.py`.
5. Click **"Deploy!"**. 
6. Your application will be live in minutes at a URL like `https://factcheck-ai.streamlit.app`.

---

## 📊 4. Machine Learning execution
- **Algorithm**: Passive Aggressive Classifier (Optimized for cloud-scale text).
- **Metric**: **99.5% Accuracy**.
- **Latency**: Sub-100ms inference time.

---

## ✅ 5. Academic Credentials
- **Lead Contributors**: DHANUSHYA E & DHARANESH VN
- **Registration**: 2303717673722009 / 2303717673721010
- **Faculty Board**: DR. SAVITHRI V, DR. CHANDIA S, DR. KAMATCHI A
- **Module**: Mobile and Cloud Application Development Lab (22MDC65)
