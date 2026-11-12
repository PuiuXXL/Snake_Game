# Student starter – Python Snake

Aceasta versiune contine aceeasi infrastructura ca backend-ul complet, insa functiile din `app/game/movement.py`, `collision.py`, `food.py` si `score.py` sunt **TODO-uri**.

Solutiile sunt deja scrise, dar comentate linie cu linie. Pentru fiecare exercitiu:

1. Citeste docstring-ul.
2. Incearca propria implementare in locul liniei `raise NotImplementedError(...)`.
3. Executa testele din `tests/`.
4. Daca te blochezi, decomenteaza implementarea de sub `TODO` si sterge `raise NotImplementedError`.

## Instalare Windows

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Teste, progresiv

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_movement.py -q
.\.venv\Scripts\python.exe -m pytest tests/test_collision.py -q
.\.venv\Scripts\python.exe -m pytest tests/test_food.py -q
.\.venv\Scripts\python.exe -m pytest tests/test_score.py -q
.\.venv\Scripts\python.exe -m pytest -q
```

## Pornire

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

`POST /api/game/start` functioneaza inainte de rezolvarea TODO-urilor. La primele tick-uri vei primi o eroare pana cand implementezi functiile necesare; este intentionat.

Vezi si `workshop/README.md` pentru explicatiile pas cu pas privind crearea proiectului, React si conectarea HTTP.
