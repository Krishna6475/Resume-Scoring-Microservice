import joblib
import json
import os
import re
BASE_DIR = r"D:\resume-scorer\resume-scorer"

class ResumeScorer:
    def __init__(self, goal):
        self.goal = goal
        model_file = f"{goal.lower().replace(' ', '_')}_model.pkl"
        
        self.model_path = os.path.join(BASE_DIR, "app", "model", model_file)
        self.vectorizer_path = os.path.join(BASE_DIR, "app", "model", "tfidf_vectorizer.pkl")
        self.goals_path = os.path.join(BASE_DIR, "data", "goals.json")
        
        self.goals = json.load(open(self.goals_path))
        self.model = joblib.load(self.model_path)
        self.vectorizer = joblib.load(self.vectorizer_path)

    def score_resume(self, resume_text):
        vector = self.vectorizer.transform([resume_text])
        score = self.model.predict_proba(vector)[0][1]
        return score

    # def extract_skills(self, resume_text):
    #     resume_words = set(word.lower() for word in resume_text.split())
    #     required = self.goals.get(self.goal, [])
    #     matched = [s for s in required if s.lower() in resume_words]
    #     missing = [s for s in required if s.lower() not in resume_words]
    #     learning_path = [f"Learn {s}" for s in missing]
    #     return matched, missing, learning_path

    def extract_skills(self, resume_text):
        resume_text_lower = resume_text.lower()
        resume_text_clean = re.sub(r'[^\w\s]', '', resume_text_lower)  # Remove punctuation
        matched = []
        missing = []

        for skill in self.goals.get(self.goal, []):
            if skill.lower() in resume_text_clean:
                matched.append(skill)
            else:
                missing.append(skill)

        learning_path = [f"Learn {s}" for s in missing]
        return matched, missing, learning_path
