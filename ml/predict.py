import joblib

model = joblib.load('model.pkl')

def predict_sentiment(text: str) -> int:
    pred = model.predict([text])
    return int(pred[0])
