from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_hello_and_health():
    assert client.get('/api/hello').json()['message'] == 'Salut din Python!'
    assert client.get('/api/health').status_code == 200


def test_complete_api_lifecycle():
    created = client.post('/api/game/start')
    assert created.status_code == 200
    game_id = created.json()['gameId']
    state = created.json()['state']
    assert state['status'] == 'running'
    assert state['boardSize'] == 20
    assert client.get(f'/api/game/{game_id}').json() == state

    # Directia inversa este ignorata de motorul Python.
    reversed_dir = client.post(f'/api/game/{game_id}/direction', json={'direction':'left'})
    assert reversed_dir.json()['direction'] == 'right'
    advanced = client.post(f'/api/game/{game_id}/tick', json={'direction': 'up'})
    assert advanced.status_code == 200
    assert advanced.json()['snake'][0] == {'x':10,'y':8}

    reset = client.post(f'/api/game/{game_id}/reset')
    assert reset.json()['score'] == 0
    assert reset.json()['snake'][0] == {'x':10,'y':9}


def test_invalid_id_and_direction():
    assert client.get('/api/game/unknown').status_code == 404
    created = client.post('/api/game/start').json()
    game_id = created['gameId']
    assert client.post(f'/api/game/{game_id}/direction', json={'direction':'diagonal'}).status_code == 422
