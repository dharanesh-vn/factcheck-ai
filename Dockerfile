# Use multi-stage build for efficiency
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -4 -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Ensure model directory exists (training should happen before or during build)
RUN mkdir -p model

# Expose ports for both Streamlit and FastAPI
EXPOSE 8501
EXPOSE 8000

# Default command starts the Streamlit app
# To run API, use: docker run -p 8000:8000 fake-news-detector python api.py
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
