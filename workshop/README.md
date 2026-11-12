# Workshop Snake Overflow: de la folder gol la joc web

## Scop si public

Participantii invata ce inseamna un frontend, un backend, un API HTTP si cum construiesti o aplicatie web folosind React + TypeScript + Vite si Python + FastAPI. Modelul educativ este inspirat de Berkeley Pacman: infrastructura este stabila, iar exercitiile de logica sunt izolate si au teste.

**Doua variante incluse in arhiva:**

1. `backend/` + `frontend/` din radacina proiectului = **joc complet, pentru demo**.
2. `workshop/starter/backend/` = **backend pentru participanti**, cu solutii comentate si TODO-uri.

## Ordinea recomandata

| Etapa | Ce construim | Ce trebuie sa vada participantul |
|---|---|---|
| 0 | Instalare Node.js, Python, VS Code | `node -v`, `npm -v`, `py --version` |
| 1 | Directorul proiectului + frontend Vite | Pagina React in browser |
| 2 | Backend FastAPI | Raspuns JSON la `/api/hello` |
| 3 | Legatura HTTP cu `fetch` | Mesaj din Python vizibil in React |
| 4 | Tabla + tastatura | Tabla Snake afisata si taste recunoscute |
| 5 | Reguli Python cu TODO | Testele unitare trec pe rand |
| 6 | Motor + sesiuni + API | Snake functional cu scor si Game Over |

## 0. Ce instalezi

- VS Code, cu extensiile Python si ESLint (optional).
- Python 3.11+ si Node.js compatibil cu Vite 8 (Node 20.19+ sau 22.12+).
- Git (optional, dar recomandat pentru commit-uri si revenirea la versiuni anterioare).

Deschide un terminal PowerShell:

```powershell
node --version
npm --version
py --version
```

## 1. Porneste un proiect complet nou

Intr-un folder de lucru:

```powershell
mkdir Snake_Game
cd Snake_Game
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
npm run dev
```

Deschide http://localhost:5173/. Interfata React exista, dar inca nu are un backend.

**Explicatie:** React descrie interfata; TypeScript verifica tipuri; Vite porneste serverul local si compileaza codul frontend.

## 2. Creeaza backend-ul de la zero

Deschide alt terminal in radacina `Snake_Game`:

```powershell
mkdir backend
cd backend
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install "fastapi[standard]"
```

Creeaza `backend/main.py` cu acest continut:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

@app.get("/api/hello")
def hello():
    return {"message": "Salut din Python!"}
```

Porneste:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

Deschide http://127.0.0.1:8000/api/hello si http://127.0.0.1:8000/docs.

**Explicatie:** FastAPI expune rute HTTP; endpoint-ul intoarce un dictionar Python convertit automat in JSON. CORS permite paginii de pe portul 5173 sa apeleze serverul de pe portul 8000.

## 3. Primul apel frontend → backend

In `frontend/src/App.tsx`, pentru **primul exercitiu**, poti inlocui temporar continutul cu:

```tsx
import { useState } from 'react'

function App() {
  const [message, setMessage] = useState('')

  const askPython = async () => {
    const response = await fetch('http://127.0.0.1:8000/api/hello')
    const data: { message: string } = await response.json()
    setMessage(data.message)
  }

  return (
    <main>
      <h1>Snake Workshop</h1>
      <button onClick={askPython}>Intreaba Python</button>
      <p>{message}</p>
    </main>
  )
}

export default App
```

Apasa butonul. Pe ecran apare **Salut din Python!**. Explica participantilor cererea `GET`, raspunsul JSON, `await`, precum si faptul ca React nu executa cod Python direct.

**Opreste-te si verifica:** functioneaza ambele servere? Este vizibil mesajul? In DevTools → Network apare request-ul?

## 4. Construim interfata Snake

Pentru lectia completa, foloseste ca **referinta** componentele existente din `frontend/src/components`, `pages`, `assets`, `config` si `types`. Explica-le pe rand, nu le prezenta pe toate simultan.

Ordinea recomandata pentru implementarea din zero:

1. Defineste `type Position = { x: number; y: number }` in `types/game.ts`.
2. Creeaza `GameBoard.tsx` cu o tabla tip CSS Grid de 20 × 20 de celule.
3. Afiseaza cateva pozitii fixe ale sarpelui (`[{x:10,y:9}, ...]`) si o pozitie pentru mancare.
4. Creeaza `GameHeader.tsx` pentru scor.
5. Foloseste `addEventListener('keydown', ...)` in React, dar **nu calcula miscarea in frontend**.
6. Adauga paginile Start si Game Over si stilurile din versiunea demonstrativa.

**Nu copia `gameRules.ts` ca implementare activa.** Originalul TypeScript se afla in `workshop/reference_typescript/`, numai pentru comparatie.

## 5. Implementam logica Snake in Python (stil Berkeley)

Cand treci de la primul endpoint demonstrativ la proiectul real, foloseste infrastructura pregatita din `workshop/starter/backend/` ca **punct de pornire** pentru backend. Poti copia continutul ei peste backend-ul minimal din lectiile 2–3 (fa mai intai un commit sau o copie).

Structura dupa aceasta etapa:

```text
Snake_Game/
├── frontend/
│   └── src/components/ ...
└── backend/
    ├── app/main.py
    ├── app/api/game.py
    ├── app/models/game.py
    ├── app/game/movement.py    # TODO + solutie comentata
    ├── app/game/collision.py   # TODO + solutie comentata
    ├── app/game/food.py        # TODO + solutie comentata
    ├── app/game/score.py       # TODO + solutie comentata
    ├── app/game/engine.py      # infrastructura deja functionala
    └── tests/
```

In `backend/` (cu venv activ/invocat explicit) instaleaza dependentele:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Apoi rezolva fiecare TODO, de exemplu:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_movement.py -q
.\.venv\Scripts\python.exe -m pytest tests/test_collision.py -q
.\.venv\Scripts\python.exe -m pytest tests/test_food.py -q
.\.venv\Scripts\python.exe -m pytest tests/test_score.py -q
```

Testele vor esua initial cu `NotImplementedError`. Asta este intentionat: participantii implementeaza functia si ruleaza din nou pana apare `PASSED`.

**Atentie:** Solutia este scrisa ca **Python real, comentat** in fiecare TODO. Daca participantii o folosesc, trebuie sa decomenteze liniile si sa elimine `raise NotImplementedError`.

## 6. Conectarea jocului, nu doar a mesajului

API-ul Python final (din proiectul livrat) are urmatorul ciclu:

```text
React: apasa START
  -> POST /api/game/start
Python: creeaza GameState + gameId
  <- JSON cu starea initiala

React: la fiecare ~140 ms (si directia tastaturii)
  -> POST /api/game/{gameId}/tick  {"direction":"right"}
Python: engine.tick() apeleaza movement/collision/food/score
  <- JSON cu sarpe, mancare, scor, status

React: redeseneaza GameBoard
  -> cand status == "game_over", arata GameOverPage
```

Foloseste `frontend/src/services/gameApi.ts` si `frontend/src/hooks/useSnakeGame.ts` din proiectul complet drept exemple finale. React trebuie doar sa trimita comenzile si sa afiseze raspunsul. Backend-ul Python este sursa de adevar pentru reguli si scor.

## 7. Verificarea proiectului final

Porneste in paralel doua terminale:

```powershell
# Terminal 1, din Snake_Game/backend
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

```powershell
# Terminal 2, din Snake_Game/frontend
npm install
npm run dev
```

Deschide http://localhost:5173/; apasa START; foloseste sagetile sau WASD; mananca, loveste un perete si verifica Game Over.

## Cateva principii utile organizatorilor

- Cere un **commit Git** inainte de modificarile mari, in special cele generate de Copilot.
- Primele lectii folosesc un singur `main.py`, apoi introduc `app/`, API, modele si module Python; evita supraincarcarea initiala.
- Lucreaza cu teste mici, dupa fiecare etapa, inainte de integrarea UI.
- Nu amesteca solutiile executabile ale profesorului cu TODO-urile studentilor in aceeasi instanta a serverului.
- Poti pregati exemple live in Git branch-uri separate pe etape, dar nu este necesar sa faci force-push sau reset distructiv.

## Diferenta fata de Berkeley Pacman

Similar: functii cu semnaturi clare, infrastructura predefinita, teste unitare, exercitii progresive. Diferit: aici participantii invata si HTTP, frontend, server, nu numai algoritmi de cautare.

## Materiale suplimentare pentru demonstratie

- [Lectia 4 – GameBoard construit de la zero](lectii/04_frontend_de_la_zero.md)
- [Lectia 5 – exercitiile Python si testele](lectii/05_exercitii_python.md)
