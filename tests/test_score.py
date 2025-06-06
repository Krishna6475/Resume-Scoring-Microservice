from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_score_endpoint():
    response = client.post("/score", json={
        "student_id": "stu_01",
        "goal": "Amazon SDE",
        "resume_text": "Experienced in Java, SQL, and Data Structures"
    })
    assert response.status_code == 200
    assert "score" in response.json()
