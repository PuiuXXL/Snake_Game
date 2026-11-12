# Snake Overflow – Backend Python (versiunea completa)

Aceasta este **versiunea functionala, pentru organizatori**. Logica jocului este in Python, iar interfata React trimite cereri JSON catre FastAPI.

## Pornire pe Windows / PowerShell

Din folderul `Snake_Game/backend`:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

- API: http://127.0.0.1:8000
- Documentatie Swagger: http://127.0.0.1:8000/docs
- Exemplu simplu: http://127.0.0.1:8000/api/hello

Pe macOS / Linux, foloseste `python3 -m venv .venv`, apoi `.venv/bin/python`.

## Teste

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Endpoint-uri

| Metoda | Endpoint | Rol |
|---|---|---|
| GET | `/api/hello` | Demo: primul mesaj Python → React |
| GET | `/api/health` | Verifica daca serverul este activ |
| POST | `/api/game/start` | Creeaza un joc; returneaza `gameId` si `state` |
| GET | `/api/game/{game_id}` | Returneaza starea curenta |
| POST | `/api/game/{game_id}/direction` | Body: `{ "direction": "up" }` |
| POST | `/api/game/{game_id}/tick` | Body optional: `{ "direction": "up" }`; avanseaza un pas |
| POST | `/api/game/{game_id}/reset` | Reporneste jocul in aceeasi sesiune |

### Exemplu de raspuns `state`

```json
{
  "boardSize": 20,
  "snake": [{"x": 10, "y": 9}, {"x": 9, "y": 9}],
  "direction": "right",
  "food": {"x": 14, "y": 6},
  "score": 0,
  "status": "running"
}
```

## Codul Python

- `app/models/game.py`: contractul JSON (Pydantic).
- `app/game/movement.py`: pozitia urmatoare, directii valide.
- `app/game/collision.py`: coliziuni cu peretele sau corpul.
- `app/game/food.py`: mancarea si celulele disponibile.
- `app/game/score.py`: scorul.
- `app/game/engine.py`: integreaza regulile la fiecare tick.
- `app/store.py`: stari independente pentru mai multe jocuri; doar in memorie.
- `app/api/game.py`: endpoint-urile HTTP.
- `app/main.py`: aplicatia FastAPI si CORS.

Nota: jocurile tinute in memorie dispar la restartul serverului. Serverul de dezvoltare nu are persistenta sau autentificare.

Pentru exercitii foloseste `workshop/starter/backend`, care contine semnaturile si codul comentat, nu acest director.
