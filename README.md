# FactCheck AI: Enterprise Distributed Cloud Architecture

## 1. Project Overview
FactCheck AI is a centralized Machine Learning as a Service (MLaaS) platform designed for the real-time detection of misinformation. The system utilizes advanced Natural Language Processing (NLP) to analyze linguistic patterns and determine the authenticity of news content.

## 2. Technical Architecture
The system follows a decoupled, distributed cloud architecture to ensure high availability, security, and scalability.

- **Presentation Layer (Frontend)**: Standardized HTML5/CSS3 interface hosted on Amazon S3.
- **Content Delivery Layer (CDN)**: Amazon CloudFront provides HTTPS encryption and global content distribution.
- **Application Layer (Backend)**: Flask-based REST API running on AWS Elastic Beanstalk (EC2).
- **Analytical Layer (AI)**: Passive Aggressive Classifier (PAC) trained on a corpus of 44,800 validated articles.

## 3. Core System Functions
- **Linguistic Inference (predict.py)**: Processes raw text through a TF-IDF vectorizer and executes the PAC model to identify structural hallmarks of fake news.
- **RESTful API (application.py)**: Manages incoming POST requests, handles data serialization, and implements strict Cross-Origin Resource Sharing (CORS) protocols.
- **Asynchronous Communication (index.html)**: Utilizes the Fetch API to perform non-blocking calls to the cloud backend, ensuring a seamless user experience.

## 4. Current Project Structure
```text
fake-news-detection/
├── app/                  # Python-based alternative dashboard
├── model/                # AI intelligence artifacts (.pkl files)
├── src/                  # Core inference and processing scripts
├── application.py        # Primary Cloud API (Flask)
├── index.html            # Primary Cloud Frontend (S3 Hosting)
├── Procfile              # AWS deployment process configuration
├── requirements.txt      # Automated dependency management
├── .gitignore            # Environment exclusion rules
└── README.md             # Technical documentation and registry
```

## 5. Live Production Links
- **Platform URL**: https://factcheck-ui-unique-name.s3.us-east-1.amazonaws.com/index.html
- **API Terminal**: https://dyzfcyb8dw1ce.cloudfront.net/predict
- **Service Status**: http://factcheck-prod.eba-shmkjjex.us-east-1.elasticbeanstalk.com/

## 6. Institutional Registry
- **Lead Developer**: Dhanushya E (2303717673722009)
- **Lead Developer**: Dharanesh VN (2303717673721010)
- **Coursework**: Mobile and Cloud Application Development Lab (22MDC65)
- **Supervisory Board**: Dr. Savithri V, Dr. Chandia S, Dr. Kamatchi A
