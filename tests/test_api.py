from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict():
    response = client.post(
        "/predict",
        json={"data": [5.1, 3.5, 1.4, 0.2]}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()
    # return response.json()