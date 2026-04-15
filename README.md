# 🛡️ FactCheck AI: Cloud-Integrated Content Verification Service

> **Project Title:** FactCheck AI | **Status:** Production-Ready | **Accuracy:** 99.5%

## 📝 1. What is FactCheck AI?
It is a high-fidelity **Fake News Detection** system that uses Natural Language Processing (NLP) to verify content as authentic or fabricated.
- **AI Engine**: Passive Aggressive Classifier.
- **Training Corpus**: 44,800 news articles.
- **Goal**: Differentiate sensationalist misinformation from factual reporting.

---

## 🏗️ 2. How the Model & Dataset are Deployed
In a professional cloud environment, deployment is split into two parts:

### **A. Training (Preprocessing Stage)**
- The large datasets (`True.csv` and `Fake.csv`) are approximately **120MB**.
- These are used **only once** to train the model locally. 
- During training, the system "learns" the patterns and saves them into two small files: **`model.pkl`** and **`vectorizer.pkl`**.
- **Important**: Once you have these `.pkl` files, you do not need the large CSV files to run the app.

### **B. Inference (Live Stage)**
- When you deploy to the Cloud, we only upload the logic (`app.py`, `src/`) and the intelligence (`model/*.pkl`).
- The cloud server loads the `.pkl` file into its memory (RAM). When a user enters text, the model uses these saved weights to provide an instant prediction.
- This results in a **highly lightweight and fast cloud service**.

---

## 🚀 3. Deployment Guide (Free)

### **Phase 1: GitHub Setup**
1. Upload all files **EXCEPT** the large `data/` folder to GitHub. (The `.gitignore` file I provided will help with this automatically).
2. Your GitHub should include: `app/`, `src/`, `model/`, `requirements.txt`, and `api.py`.

### **Phase 2: Streamlit Cloud**
1. Connect your repo at [share.streamlit.io](https://share.streamlit.io/).
2. Deploy using `app/app.py`.

---

## ⚠️ 4. Troubleshooting "Error Installing Requirements"
If your deployment fails during installation:
1. **Remove Version Numbers**: Ensure your `requirements.txt` only lists package names (e.g., `pandas`, not `pandas==1.5.0`). I have updated it for you.
2. **Delete Data Folder**: Do not push the 120MB CSV files to GitHub. Large files can cause server timeouts during the environment build phase.
3. **NLTK Data**: The system automatically downloads NLTK stopwords on the first run.

---

## 📊 5. Machine Learning Specs
- **Algorithm**: Passive Aggressive Classifier.
- **Accuracy**: 99.5%.
- **Latency**: Sub-100ms.

---

## ✅ 6. Academic Credentials
- **Lead Contributors**: DHANUSHYA E & DHARANESH VN
- **Registration**: 2303717673722009 / 2303717673721010
- **Faculty Board**: DR. SAVITHRI V, DR. CHANDIA S, DR. KAMATCHI A
- **Module**: Mobile and Cloud Application Development Lab (22MDC65)
