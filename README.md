# 🧠 Resume Scoring Microservice

A production-ready, containerized microservice that evaluates student resumes against specified career goals and returns:
- ✅ A numerical match score (from a trained ML model)
- ✅ A list of matched and missing skills
- ✅ A suggested learning path to bridge skill gaps

> This project runs fully offline and is deployable using Docker.

---

## 🚀 Features

- Accepts structured JSON input
- Scores resumes using TF-IDF + Logistic Regression
- Provides skill-level feedback and learning paths
- Fully offline, no external API calls
- Lightweight FastAPI backend
- Dockerized for deployment

---

## 📥 Input (POST `/score`)

```json
{
  "student_id": "stu_1084",
  "goal": "Amazon SDE",
  "resume_text": "Final year student skilled in Java, Python, DSA, SQL, REST APIs..."
}
