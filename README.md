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

## 📥 Input Fields

| Field        | Type   | Required | Description                          |
|--------------|--------|----------|--------------------------------------|
| student_id   | string | ✅        | Unique student identifier            |
| goal         | string | ✅        | Target role or domain (e.g., ML Internship) |
| resume_text  | string | ✅        | Resume content in plain text         |

---

## 📤 Output (JSON Response)

```json
{
  "score": 0.81,
  "matched_skills": ["Java", "DSA", "SQL"],
  "missing_skills": ["System Design"],
  "suggested_learning_path": [
    "Learn basic system design concepts",
    "Complete SQL joins and indexing course"
  ]
}

# ⚙️ API Endpoints

| Method | Endpoint    | Description                       |
|--------|-------------|-----------------------------------|
| POST   | `/score`    | Evaluate resume and return results|
| GET    | `/health`   | Check service health              |
| GET    | `/version`  | Show model and config metadata    |

---

# 🧠 Model Architecture

- 🔢 **TF-IDF Vectorizer + Logistic Regression**
- 📌 **Binary classifier per goal** (e.g., "Amazon SDE")
- 🎯 **Inputs**: Resume text
- 📈 **Outputs**: Score ∈ [0.0, 1.0]
- ⚙️ **Controlled by**: `config.json`

# 🗃️ Training Data Format

```json
[
  {
    "goal": "Amazon SDE",
    "resume_text": "Java, C++, REST APIs, DS",
    "label": 1
  },
  {
    "goal": "Amazon SDE",
    "resume_text": "Mechanical CAD, AutoDesk, Civil Design",
    "label": 0
  }
]

# 📚 Skill Logic (`goals.json`)

```json
{
  "Amazon SDE": ["Java", "Data Structures", "System Design", "SQL"],
  "ML Internship": ["Python", "Numpy", "Scikit-learn", "Linear Algebra"]
}

# 🔍 Used for

- ✅ **matched_skills**: Detected from resume  
- ❌ **missing_skills**: Not found but required  
- 📘 **suggested_learning_path**: Hardcoded per missing skill  

# 🗂️ Project Structure

resume-scorer/
├── app/
│ ├── main.py
│ ├── scorer.py
│ └── model/
│ ├── amazon_sde_model.pkl
│ └── tfidf_vectorizer.pkl
├── data/
│ ├── training_amazon_sde.json
│ └── goals.json
├── config.json
├── Dockerfile
├── requirements.txt
├── README.md
├── schema.json
└── tests/
└── test_score.py

# ⚙️ Sample `config.json`

```json
{
  "version": "1.0.0",
  "minimum_score_to_pass": 0.6,
  "log_score_details": true,
  "model_goals_supported": ["Amazon SDE", "ML Internship"],
  "default_goal_model": "Amazon SDE"
}

# 🔎 Defines

- **Minimum passing score**
- **Logging behavior**
- **Supported goals**
- **Default goal fallback**

> ❗ *App will fail if config is missing or invalid.*

# 🐳 Docker Instructions

Build and run the containerized microservice:

```bash
# Build the Docker image
docker build -t resume-scorer .

# Run the Docker container
docker run -p 8000:8000 resume-scorer

# 📄 License

This project is for educational and internal use only.  
Available under the **MIT License**.

---

# ✍️ Author

**Chinthagunta Vamshi Krishna**  
B.Tech in CSE (AI & ML), 
Institute of Aeronautical Engineering  
Email: vamshikrishna6475@gmail.com

---

# 🙌 Acknowledgements

This project was completed as part of a technical internship assignment under the guidance of **Turtil Technologies**.
