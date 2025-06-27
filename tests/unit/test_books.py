from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book():
    response = client.post("/books/", json={"title": "Book A", "author": "Author A"})
    assert response.status_code == 200
    assert response.json()["title"] == "Book A"
