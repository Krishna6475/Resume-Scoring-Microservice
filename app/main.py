from fastapi import FastAPI
from pydantic import BaseModel
import json
from app.scorer import ResumeScorer

# Load config
CONFIG_PATH = r"D:\resume-scorer\resume-scorer\config.json"
with open(CONFIG_PATH) as f:
    config = json.load(f)

app = FastAPI()

class ResumeRequest(BaseModel):
    student_id: str
    goal: str
    resume_text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": config["version"]}

@app.post("/score")
def score(req: ResumeRequest):
    if req.goal not in config["model_goals_supported"]:
        return {"error": "Unsupported goal"}

    scorer = ResumeScorer(req.goal)
    score = scorer.score_resume(req.resume_text)
    matched, missing, path = scorer.extract_skills(req.resume_text)

    return {
        "score": round(score, 2),
        "matched_skills": matched,
        "missing_skills": missing,
        "suggested_learning_path": path
    }
