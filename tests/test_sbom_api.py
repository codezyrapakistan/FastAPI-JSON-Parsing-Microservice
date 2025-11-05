from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_endpoint():
    response = client.post("/api/analyze", json={
        "components": [
            {"name": "flask", "version": "2.0.1", "license": "MIT"}
        ]
    })
    assert response.status_code == 200
    assert "results" in response.json()
