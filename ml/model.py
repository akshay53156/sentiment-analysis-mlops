import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_and_save_model():
    # Sample data (replace with your own or dataset loading)
    texts = ["I love this product", "This is the worst", "Amazing experience", "Not good"]
    labels = [1, 0, 1, 0]  # 1=Positive, 0=Negative
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', LogisticRegression())
    ])
    pipeline.fit(texts, labels)
    joblib.dump(pipeline, 'model.pkl')

if __name__ == "__main__":
    train_and_save_model()
