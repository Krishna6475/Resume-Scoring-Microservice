import json
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Updated path
TRAIN_DATA_PATH = r"D:\resume-scorer\resume-scorer\data\training_amazon_sde.json"
MODEL_DIR = r"D:\resume-scorer\resume-scorer\app\model"

# Load data
with open(TRAIN_DATA_PATH, "r") as f:
    data = json.load(f)

texts = [item["resume_text"] for item in data]
labels = [item["label"] for item in data]

# Train
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
model = LogisticRegression()
model.fit(X, labels)

# Save
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(vectorizer, os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"))
joblib.dump(model, os.path.join(MODEL_DIR, "amazon_sde_model.pkl"))
