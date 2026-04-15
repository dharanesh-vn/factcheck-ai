from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import sys

# Add src to path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)

from predict import predict_news

app = FastAPI(title="Fake News Detection API", description="Cloud-ready API for news verification")

class NewsItem(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Fake News Detection API is online", "status": "Ready"}

@app.post("/predict")
def predict(item: NewsItem):
    if not item.text:
        raise HTTPException(status_code=400, detail="No text provided")
    
    result = predict_news(item.text)
    return {
        "prediction": result,
        "is_real": result == "REAL"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
