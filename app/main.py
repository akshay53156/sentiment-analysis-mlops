from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ml.predict as predict_module

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(request: TextRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    result = predict_module.predict_sentiment(request.text)
    sentiment = "positive" if result == 1 else "negative"
    return {"sentiment": sentiment}
