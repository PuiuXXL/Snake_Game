"""Teste pentru rute (merg si pe scheletul gol)."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_new_game_works_without_any_level():
    response = client.post("/game/new")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "running"
    assert len(body["snake"]) == 4


def test_new_game_rejects_bad_board_size():
    assert client.post("/game/new?board_size=1").status_code == 422
