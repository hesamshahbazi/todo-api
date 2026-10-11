import os
import tempfile
from pathlib import Path
from fastapi.testclient import TestClient

_db = tempfile.TemporaryDirectory()
os.environ["DATABASE_URL"] = "sqlite:///" + str(Path(_db.name) / "nested" / "test.db")
from app.main import app


def test_crud_and_validation():
    with TestClient(app) as client:
        for title in ["", "  ", "x" * 501]:
            assert client.post("/tasks", json={"title": title}).status_code == 422
        task = client.post("/tasks", json={"title": "  Learn SQL  "}).json()
        assert task["title"] == "Learn SQL"
        url = f"/tasks/{task['id']}"
        assert client.get(url).json() == task
        assert client.put(url, json={"is_done": True}).json()["is_done"] is True
        assert client.put(url, json={"title":" "}).status_code == 422
        assert any(t["id"] == task["id"] for t in client.get("/tasks").json())
        assert client.delete(url).status_code == 200
        assert client.get(url).status_code == 404
        assert client.put(url, json={"title":"missing"}).status_code == 404
        assert client.delete(url).status_code == 404
