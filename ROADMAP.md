# Roadmap: ce modificăm în Python, în ce ordine, ce se întâmplă și ce spunem

> Conține **soluțiile complete**. Nu-l da participanților.

Pornire (o singură dată): `cd backend && python -m uvicorn main:app --reload --port 8000`
și `cd frontend && npm run dev`, apoi `http://localhost:5173`.
După fiecare pas: salvezi, serverul se reîncarcă singur, în browser apeși Start și rulezi testul.

Ordinea: `movement.py` → `engine.py` → `movement.py` → `engine.py` → `collisions.py` →
`engine.py` → `collisions.py` → `engine.py` → `food.py` → `engine.py`.

Fiecare pas are: **Codul de la care pornim**, **Codul nou**, **Ce se vede** și **De spus**.

---

## Pasul 1: `movement.py` (`next_head`) + `engine.py` (`step` minim)

**Codul de la care pornim**

`backend/game/movement.py`:

```python
def next_head(head: Position, direction: Direction) -> Position:
    raise NotImplementedError("Nivel 1: completeaza next_head (game/movement.py)")
```

`backend/game/engine.py`:

```python
def step(state: GameState, requested: Direction) -> GameState:
    """...(docstring cu cei 7 pași)..."""
    raise NotImplementedError("Nivel 6: completeaza step (game/engine.py)")
```

**Codul nou**

`backend/game/movement.py`:

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

`backend/game/engine.py` (înlocuiește corpul lui `step`):

```python
def step(state: GameState, requested: Direction) -> GameState:
    new_head = next_head(state.snake[0], state.direction)
    new_snake = [new_head] + state.snake[:-1]
    return state.model_copy(update={"snake": new_snake})
```

- Test: `pytest -k nivel1`
- **Ce se vede:** șarpele merge singur spre dreapta și **iese de pe tablă**. Tastele nu fac nimic.

**De spus**
- Frontend-ul trimite starea la fiecare ~140 ms, iar `step` întoarce starea nouă. Backend-ul nu ține minte nimic.
- Originea (0,0) e în **stânga-sus**: `up` scade `y`, `down` crește `y`.
- Mișcarea = adaugi capul nou în față și scoți coada. Corpul nu „se mută" celulă cu celulă.
- `model_copy` face o copie, nu modificăm starea primită.

## Pasul 2: `movement.py` (`is_opposite`) + `engine.py` (`step` cu direcție)

**Codul de la care pornim**

`backend/game/movement.py`:

```python
def is_opposite(current: Direction, requested: Direction) -> bool:
    raise NotImplementedError("Nivel 2: completeaza is_opposite (game/movement.py)")
```

`backend/game/engine.py`: `step` din pasul 1 (folosește mereu `state.direction`).

**Codul nou**

`backend/game/movement.py`:

```python
def is_opposite(current: Direction, requested: Direction) -> bool:
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    return opposites[current] == requested
```

`backend/game/engine.py`:

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
- **Ce se vede:** tastele schimbă direcția. Opusul direcției curente e ignorat. Încă iese de pe tablă.

**De spus**
- Până acum `requested` nu era folosit, acum e tasta apăsată.
- Fără `is_opposite`, șarpele s-ar întoarce pe loc și s-ar mușca singur. Întreabă sala de ce.
- Un dicționar e mai clar decât patru `if`-uri.

## Pasul 3: `collisions.py` (`hits_wall`) + `engine.py` (`step` cu perete)

**Codul de la care pornim**

`backend/game/collisions.py`:

```python
def hits_wall(head: Position, board_size: int) -> bool:
    raise NotImplementedError("Nivel 3: completeaza hits_wall (game/collisions.py)")
```

`backend/game/engine.py`: `step` din pasul 2 (fără verificare de status, fără coliziuni).

**Codul nou**

`backend/game/collisions.py`:

```python
def hits_wall(head: Position, board_size: int) -> bool:
    return (
        head.x < 0 or head.x >= board_size
        or head.y < 0 or head.y >= board_size
    )
```

`backend/game/engine.py`:

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
- **Ce se vede:** lovești peretele și apare pagina **Game Over**. Momentul „wow" al workshopului.

**De spus**
- `status` e cum îi spunem frontend-ului ce ecran să arate: `running` sau `game_over`.
- Capcană clasică: `>= board_size` (nu `>`), pentru că ultima celulă are indexul `board_size - 1`.
- Verificăm capul **nou**, înainte să mutăm șarpele.
- Dacă jocul s-a terminat, `step` întoarce starea neschimbată.

## Pasul 4: `collisions.py` (`hits_self`) + `engine.py` (`step` cu corp)

**Codul de la care pornim**

`backend/game/collisions.py`:

```python
def hits_self(head: Position, body: list[Position]) -> bool:
    raise NotImplementedError("Nivel 4: completeaza hits_self (game/collisions.py)")
```

`backend/game/engine.py`: `step` din pasul 3 (doar `hits_wall`).

**Codul nou**

`backend/game/collisions.py`:

```python
def hits_self(head: Position, body: list[Position]) -> bool:
    return head in body
```

`backend/game/engine.py` (înlocuiește verificarea de perete):

```python
    body = state.snake[:-1]   # coada se mută, deci nu o socotim
    if hits_wall(new_head, state.boardSize) or hits_self(new_head, body):
        return state.model_copy(update={"status": "game_over"})
```

- Test: `pytest -k nivel4`
- **Ce se vede:** dacă șarpele se întoarce peste el (dreapta → jos → stânga → sus) apare Game Over.

**De spus**
- `head in body` merge pentru că `Position` e `frozen`: două poziții cu aceleași `x`, `y` sunt egale.
- De ce `snake[:-1]`? Coada se mută în același pas, deci capul poate intra în celula ei.

## Pasul 5: `food.py` (`spawn_food`)

**Codul de la care pornim**

`backend/game/food.py`:

```python
def spawn_food(board_size: int, snake: list[Position]) -> Position | None:
    raise NotImplementedError("Nivel 5: completeaza spawn_food (game/food.py)")
```

**Codul nou**

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

- Test: `pytest -k nivel5`
- **Ce se vede:** nimic în joc, `step` nu o apelează încă. Se vede doar în teste.

**De spus**
- De ce nu alegem direct un `random` pe toată tabla? Ar putea nimeri șarpele.
- Facem lista celulelor **libere** și alegem una.
- Returnăm `None` când tabla e plină (jocul e câștigat).

## Pasul 6: `engine.py` (`step` final: mănâncă și crește)

**Codul de la care pornim**

`backend/game/engine.py`: `step` din pasul 4 (mișcare, direcție, perete, corp, fără mâncare).

**Codul nou**

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

- Test: `pytest -q` → toate verzi.
- **Ce se vede:** mănânci mărul, scorul crește cu 10, șarpele se lungește, apare alt măr. Jocul e complet.

**De spus**
- Creșterea = nu scoatem coada. Asta e toată diferența dintre `ate` și `not ate`.
- Mâncarea nouă se alege pe `new_snake`, ca să nu apară sub șarpe.
- Recapitulare: am legat toate funcțiile mici într-una singură (`step`). Frontend-ul n-a fost modificat deloc.

---

## Dacă ceva nu merge

- `uvicorn` nu e recunoscut: `python -m uvicorn main:app --reload --port 8000`.
- Un test pică: `pytest -k nivelN` arată ce așteaptă.
- Pagina rămâne pe „Se conectează la backend…": backend-ul nu rulează sau portul 8000 e ocupat.
- Ecran alb după o modificare în frontend: oprește și repornește `npm run dev`.
