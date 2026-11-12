# Roadmap de prezentare (doar pentru prezentator)

> Acest fișier conține **soluțiile complete**. Nu-l da participanților: ține-l local
> sau scoate-l din branch-ul pe care îl distribui.

Durată estimată: ~15 min explicații + ~60 min implementare. Fiecare etapă de cod are un
rezultat **vizibil în joc**, ca participanții să vadă imediat ce au făcut.

## Pregătire (înainte de sală)

```bash
cd backend && pip install -r requirements.txt && uvicorn main:app --reload --port 8000
```
```bash
cd frontend && npm install && npm run dev
```

- Copiază `frontend/.env.example` în `frontend/.env` pe fiecare laptop.
- Deschide `http://localhost:5173` și `http://localhost:8000/docs`.
- Verifică: Start arată tabla cu șarpele înghețat și mesajul „Jocul nu se poate mișca încă".
- Ai `pytest` funcțional: `cd backend && pytest -q` (la început pică 23 de teste, e normal).

---

# PARTEA 1 — Explicația codului (de sus în jos)

Ordine: **imaginea de ansamblu → ce vede utilizatorul → cum vorbesc cele două părți → cine
decide regulile → unde lucrăm noi**.

## 1.1 Imaginea de ansamblu (2 min)

Desenează pe tablă:

```
Browser (React)  ──POST /game/step {state, direction}──▶  FastAPI (Python)
                 ◀────────── noua stare (JSON) ─────────
```

Mesajul-cheie: **frontend-ul doar desenează și trimite tastele; backend-ul decide regulile**
(mișcare, coliziuni, mâncare, scor). Frontend-ul nu știe nimic despre Snake. Mai mult:
backend-ul nu ține minte nimic între cereri, starea circulă în ambele sensuri.

## 1.2 Frontend, ce vede utilizatorul (4 min)

Deschide în ordine:

1. `frontend/src/App.tsx`: alege ecranul: `StartPage` → `GameScreen` → `GameOverPage`.
2. `frontend/src/types/game.ts`: tipurile `Position`, `Direction`, `GameState`. **Contractul**:
   ce trimite și ce primește backend-ul.
3. `frontend/src/components/GameBoard/GameBoard.tsx`: desenează grila din
   `boardSize`, `snake`, `food`. Observă: nu are nicio regulă de joc.
4. `frontend/src/hooks/useKeyboardControls.ts`: tastele → `Direction`.
5. `frontend/src/hooks/useGame.ts`: **inima frontend-ului**: la Start cere un joc nou, apoi
   la fiecare ~140 ms trimite starea + direcția și pune răspunsul în state.
6. `frontend/src/services/gameApi.ts` + `http.ts`: cele două apeluri HTTP.

## 1.3 Backend, cum e organizat (4 min)

Arată arborele:

```
backend/
├── main.py            # intrarea: uvicorn main:app
├── app/               # API-ul (gata făcut): rute, servicii, setări
└── game/              # logica jocului: AICI lucrăm
```

1. `app/routers/game.py`: două rute: `POST /game/new` și `POST /game/step`.
2. `app/services/game_service.py`: stratul subțire dintre rută și joc.
3. `game/models.py`: `Position` și `GameState`, **oglinda** lui `types/game.ts` din frontend.
4. Deschide `http://localhost:8000/docs`, apasă **Try it out** pe `/game/new` și arată JSON-ul.
   Apoi pe `/game/step` (răspuns 501): „funcția nu e scrisă încă".

## 1.4 Cum se leagă (2 min)

Urmărește **o singură apăsare de tastă** de la un capăt la altul:

> tastă `↓` → `useKeyboardControls` → `directionRef` din `useGame` → `stepGame()` →
> `POST /game/step` → `routers/game.py` → `game_service.advance_game` → **`engine.step`**
> → JSON → `setGame` → `GameBoard` se redesenează.

Ultimul pas e tot ce lipsește: `engine.step`. Pornește jocul și arată: tabla apare, nimic
nu se mișcă, pentru că `step` aruncă `NotImplementedError`.

## 1.5 Regulile și testele (3 min)

- Coordonate: **(0,0) e în stânga-sus**; `up` scade `y`, `down` crește `y`.
- `game/movement.py`, `collisions.py`, `food.py`, `engine.py`: funcții mici, cu docstring.
- `pytest -q` → 23 de teste pică. Fiecare test are „nivelul" lui: `pytest -k nivel1`.
  **Obiectiv:** să le facem verzi, pe rând.

---

# PARTEA 2 — Implementarea împreună

Strategia: construim `step` **bucată cu bucată** și, la fiecare etapă, implementăm funcția
mică de care are nevoie. Așa fiecare pas se vede în joc, nu doar în teste.

După fiecare etapă: salvezi, `uvicorn --reload` se reîncarcă singur, în browser apeși
Start (sau „Încearcă din nou") și rulezi testul nivelului.

## Etapa A — Nivel 1: șarpele se mișcă

În `game/movement.py`:

```python
def next_head(head: Position, direction: Direction) -> Position:
    if direction == "up":
        return Position(x=head.x, y=head.y - 1)
    if direction == "down":
        return Position(x=head.x, y=head.y + 1)
    if direction == "left":
        return Position(x=head.x - 1, y=head.y)
    return Position(x=head.x + 1, y=head.y)
```

În `game/engine.py` înlocuiește corpul lui `step` cu varianta minimă:

```python
def step(state: GameState, requested: Direction) -> GameState:
    new_head = next_head(state.snake[0], state.direction)
    new_snake = [new_head] + state.snake[:-1]
    return state.model_copy(update={"snake": new_snake})
```

- Test: `pytest -k nivel1`
- **Se vede:** șarpele merge spre dreapta și **iese de pe tablă** (nu există pereți încă).
  Discuție: de ce `[new_head] + snake[:-1]`? (capul se adaugă în față, coada se scoate.)
  Tastele nu fac încă nimic.

## Etapa B — Nivel 2: tastele schimbă direcția

În `game/movement.py`:

```python
def is_opposite(current: Direction, requested: Direction) -> bool:
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    return opposites[current] == requested
```

În `step`, folosește direcția cerută:

```python
def step(state: GameState, requested: Direction) -> GameState:
    direction = requested
    if is_opposite(state.direction, requested):
        direction = state.direction

    new_head = next_head(state.snake[0], direction)
    new_snake = [new_head] + state.snake[:-1]
    return state.model_copy(update={"snake": new_snake, "direction": direction})
```

- Test: `pytest -k nivel2`
- **Se vede:** șarpele virează la săgeți/WASD; dacă apeși direcția opusă, nu se întoarce.
  Întrebare pentru sală: ce s-ar întâmpla fără `is_opposite`? (șarpele s-ar mușca singur.)

## Etapa C — Nivel 3: pereții

În `game/collisions.py`:

```python
def hits_wall(head: Position, board_size: int) -> bool:
    return (
        head.x < 0 or head.x >= board_size
        or head.y < 0 or head.y >= board_size
    )
```

În `step`, după calculul capului nou:

```python
def step(state: GameState, requested: Direction) -> GameState:
    if state.status != "running":
        return state

    direction = requested
    if is_opposite(state.direction, requested):
        direction = state.direction

    new_head = next_head(state.snake[0], direction)

    if hits_wall(new_head, state.boardSize):
        return state.model_copy(update={"status": "game_over"})

    new_snake = [new_head] + state.snake[:-1]
    return state.model_copy(update={"snake": new_snake, "direction": direction})
```

- Test: `pytest -k nivel3`
- **Se vede:** lovești peretele → apare pagina **Game Over**. Momentul „wow" al workshopului.
- Capcană clasică: `>= board_size` (nu `>`), pentru că ultima celulă are indexul `board_size - 1`.

## Etapa D — Nivel 4: coliziunea cu corpul

În `game/collisions.py`:

```python
def hits_self(head: Position, body: list[Position]) -> bool:
    return head in body
```

În `step`, adaugă (după `hits_wall`):

```python
    body = state.snake[:-1]   # coada se mută, deci nu o socotim
    if hits_wall(new_head, state.boardSize) or hits_self(new_head, body):
        return state.model_copy(update={"status": "game_over"})
```

- Test: `pytest -k nivel4`
- **Se vede:** dacă șarpele se întoarce peste el (ex. dreapta → jos → stânga → sus) → Game Over.
- Discuție: de ce `head in body` merge? `Position` e `frozen`, deci două poziții cu aceleași
  `x`, `y` sunt egale.

## Etapa E — Nivel 5: mâncarea

În `game/food.py`:

```python
def spawn_food(board_size: int, snake: list[Position]) -> Position | None:
    free = []
    for x in range(board_size):
        for y in range(board_size):
            cell = Position(x=x, y=y)
            if cell not in snake:
                free.append(cell)

    if not free:
        return None
    return random.choice(free)
```

- Test: `pytest -k nivel5` (încă nu se vede în joc; nu e apelată de `step`).
- Discuție scurtă: de ce nu alegem direct `random` pe toată tabla? (ar nimeri șarpele.)

## Etapa F — Nivel 6: `step` final (mănâncă și crește)

Versiunea completă a lui `step` din `game/engine.py`:

```python
def step(state: GameState, requested: Direction) -> GameState:
    if state.status != "running":
        return state

    direction = requested
    if is_opposite(state.direction, requested):
        direction = state.direction

    new_head = next_head(state.snake[0], direction)
    ate = new_head == state.food

    # dacă n-a mâncat, coada se mută, deci poți intra în celula ei
    body = state.snake if ate else state.snake[:-1]
    if hits_wall(new_head, state.boardSize) or hits_self(new_head, body):
        return state.model_copy(update={"status": "game_over"})

    if ate:
        new_snake = [new_head] + state.snake          # crește: coada rămâne
        score = state.score + 10
        food = spawn_food(state.boardSize, new_snake)
    else:
        new_snake = [new_head] + state.snake[:-1]
        score = state.score
        food = state.food

    return state.model_copy(
        update={
            "snake": new_snake,
            "direction": direction,
            "food": food,
            "score": score,
        }
    )
```

- Test: `pytest -q` → **toate verzi (26 teste)**.
- **Se vede:** mănânci mărul → scorul crește cu 10, șarpele se lungește, apare alt măr.

---

# PARTEA 3 — Bonus (dacă mai e timp)

| Idee | Unde | Dificultate |
|---|---|---|
| Viteză care crește cu scorul | frontend: `TICK_MS` în `hooks/useGame.ts` | ușor |
| Tablă mai mare/mică | `?board_size=` la `POST /game/new` (5-50) | ușor |
| Mere speciale (+50) sau bombă | `game/food.py` + `engine.py`; sprite-urile există deja în `public/assets/png` | mediu |
| Pereți în interiorul tablei | `collisions.py` + un câmp nou `walls` în `models.py` și `types/game.ts` | mediu |
| Un endpoint nou `GET /score-tips` | `app/routers/` + înregistrat în `app/main.py` | ușor |
| Scor maxim salvat | `localStorage` în frontend | ușor |

# Plan B, dacă ceva nu merge

- **Pagina rămâne pe „Se conectează la backend…"**: backend-ul nu rulează sau portul 8000 e ocupat.
- **Ecran alb după o modificare în frontend**: oprește și repornește `npm run dev`.
- **Un participant e blocat**: `pytest -k nivelN` îi spune exact ce așteaptă testul; soluția
  etapei e în acest fișier.
- **`uvicorn` nu e recunoscut**: `python -m uvicorn main:app --reload --port 8000`.
