import json
import os
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# --- Config ---
goal_configs = {
    "Amazon SDE": r"C:\Users\hp\Downloads\resume-scorer\resume-scorer\data\training_amazon_sde.json",
    "ML Internship": r"C:\Users\hp\Downloads\resume-scorer\resume-scorer\data\training_ml_internship.json",
    "GATE ECE": r"C:\Users\hp\Downloads\resume-scorer\resume-scorer\data\training_gate_ece.json"
}

model_dir = r"C:\Users\hp\Downloads\resume-scorer\resume-scorer\app\model"
os.makedirs(model_dir, exist_ok=True)

# --- Train model for each goal ---
for goal, data_path in goal_configs.items():
    print(f"\n🚀 Training model for goal: {goal}")

    # --- Load dataset ---
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [entry["resume_text"] for entry in data]
    labels = [entry["label"] for entry in data]

    # --- TF-IDF Vectorization ---
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    y = np.array(labels)

    # Save the vectorizer
    vec_filename = f"{goal.lower().replace(' ', '_')}_vectorizer.pkl"
    vectorizer_path = os.path.join(model_dir, vec_filename)
    joblib.dump(vectorizer, vectorizer_path)
    print(f"✅ TF-IDF vectorizer saved: {vectorizer_path}")

    # --- Train/Test Split ---
    if len(y) >= 5:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, stratify=y, test_size=0.2, random_state=42
        )
    else:
        X_train, X_test, y_train, y_test = X, X, y, y
        print("⚠️ Dataset too small, using full set for both training and testing.")

    # --- Train model ---
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # --- Evaluate model ---
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)

    print(f"🎯 Training Accuracy: {train_accuracy:.4f}")
    print(f"🎯 Testing Accuracy:  {test_accuracy:.4f}")

    print("\n📊 Classification Report:\n", classification_report(y_test, y_test_pred))

    # --- Save model ---
    model_filename = f"{goal.lower().replace(' ', '_')}_model.pkl"
    model_path = os.path.join(model_dir, model_filename)
    joblib.dump(model, model_path)
    print(f"📦 Model saved: {model_path}")
