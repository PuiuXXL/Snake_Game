import type { GameState } from '../../types/game'
import { GameBoard } from '../GameBoard/GameBoard'
import { GameHeader } from '../GameHeader/GameHeader'
import './GameScreen.css'

type GameScreenProps = {
  game: GameState
}

export function GameScreen({ game }: GameScreenProps) {
  return (
    <main className="game-screen">
      <GameHeader score={game.score} />
      <GameBoard
        boardSize={game.boardSize}
        snake={game.snake}
        food={game.food}
      />
      <p className="game-screen__hint">Săgeți sau WASD pentru mișcare</p>
    </main>
  )
}
