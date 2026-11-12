# Lectia 4: primul GameBoard, construit de la zero

Inainte de a importa proiectul final cu design complex, este util ca fiecare participant sa inteleaga ce inseamna o tabla si cum React afiseaza pozitii.

**Premisa:** ai deja proiectul nou creat cu `npm create vite@latest frontend -- --template react-ts`, serverul pornit prin `npm run dev` si ai testat cu succes `/api/hello`.

## Pasul A: datele unei celule

Creeaza `frontend/src/types/game.ts`:

```ts
export type Position = { x: number; y: number }

export type Direction = 'up' | 'down' | 'left' | 'right'

export type GameState = {
  boardSize: number
  snake: Position[]
  direction: Direction
  food: Position | null
  score: number
  status: 'ready' | 'running' | 'game_over'
}
```

Coordonatele `x` si `y` incep de la 0. Pentru `boardSize=20`, coordonatele valide sunt de la 0 la 19 inclusiv.

## Pasul B: tabla statica

Creeaza `frontend/src/components/Board.tsx`:

```tsx
import type { GameState } from '../types/game'

type Props = { game: GameState }

export function Board({ game }: Props) {
  const cells = Array.from({ length: game.boardSize ** 2 }, (_, index) => {
    const x = index % game.boardSize
    const y = Math.floor(index / game.boardSize)
    const snake = game.snake.some(part => part.x === x && part.y === y)
    const food = game.food?.x === x && game.food?.y === y

    return (
      <div
        key={`${x}-${y}`}
        style={{
          background: snake ? '#6be44b' : food ? '#ff5656' : (x + y) % 2 ? '#1d3d22' : '#254e2c',
          aspectRatio: '1',
        }}
      />
    )
  })

  return (
    <div style={{
      display: 'grid',
      gridTemplateColumns: `repeat(${game.boardSize}, 1fr)`,
      width: 'min(90vw, 520px)',
      border: '4px solid #6be44b',
    }}>
      {cells}
    </div>
  )
}
```

In `frontend/src/App.tsx`, foloseste initial date fixe:

```tsx
import { Board } from './components/Board'
import type { GameState } from './types/game'

const preview: GameState = {
  boardSize: 20,
  snake: [{ x: 10, y: 9 }, { x: 9, y: 9 }, { x: 8, y: 9 }],
  direction: 'right',
  food: { x: 14, y: 6 },
  score: 0,
  status: 'ready',
}

export default function App() {
  return <main><h1>Snake</h1><Board game={preview} /></main>
}
```

**Rezultat asteptat:** vezi o tabla cu 20 × 20 de celule, un sarpe verde si mancare rosie. Inca nu exista miscare.

## Pasul C: tabla alimentata de Python

Porneste versiunea backend **completa** (`backend/`) pana cand participantii termina TODO-urile lor. Apoi inlocuieste `App.tsx` cu:

```tsx
import { useState } from 'react'
import { Board } from './components/Board'
import type { GameState } from './types/game'

type StartedGame = { gameId: string; state: GameState }

export default function App() {
  const [game, setGame] = useState<GameState | null>(null)
  const [gameId, setGameId] = useState<string | null>(null)

  async function start() {
    const response = await fetch('http://127.0.0.1:8000/api/game/start', { method: 'POST' })
    const data: StartedGame = await response.json()
    setGameId(data.gameId)
    setGame(data.state)
  }

  async function step() {
    if (!gameId) return
    const response = await fetch(`http://127.0.0.1:8000/api/game/${gameId}/tick`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ direction: 'right' }),
    })
    const data: GameState = await response.json()
    setGame(data)
  }

  return (
    <main>
      <h1>Snake</h1>
      <button onClick={() => void start()}>START</button>
      <button onClick={() => void step()} disabled={!gameId}>PAS</button>
      {game && <><p>Scor: {game.score}</p><Board game={game} /></>}
    </main>
  )
}
```

**Rezultat asteptat:** START creeaza jocul Python; fiecare click pe PAS muta sarpele o singura celula spre dreapta. Dupa cateva click-uri loveste peretele. Profesorul arata obiectele JSON in tabul Network al browserului.

## Pasul D: de la PAS manual la joc complet

Explica rolul lui `setInterval`, al evenimentelor `keydown` si faptul ca o cerere HTTP poate fi inca in curs cand vine urmatorul tick. Varianta completa din `frontend/src/hooks/useSnakeGame.ts` demonstreaza un timer cu o singura cerere activa si trimiterea ultimei directii tastate.

Pentru aspectul final (sprites, paginile Start si Game Over, CSS), arata componentele originale din `frontend/src/components`, `frontend/src/pages` si `frontend/src/assets`. Acestea nu fac calcule pentru coliziuni sau scor.
