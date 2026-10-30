### i want to try with fastapi

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn
from feature_extraction import extract_url_features

app = FastAPI(title="Phishing Detection")

model = joblib.load('best_model.joblib')

class URLRequest(BaseModel):
    url: str

@app.post("/predict")
def predict(request: URLRequest):
    features = extract_url_features(request.url)
    features_df = pd.DataFrame([features])

    prediction = int(model.predict(features_df)[0])
    probabilities = model.predict_proba(features_df)[0]

    return {
        "url": request.url,
        "prediction": "legitimate" if prediction == 1 else "phishing",
        "phishing_probability": round(float(probabilities[0]), 6),
        "legitimate_probability": round(float(probabilities[1]), 6),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)