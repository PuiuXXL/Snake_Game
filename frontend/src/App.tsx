import './App.css'

import { StartPage } from './pages/StartPage'
import { GameOverPage } from './pages/GameOverPage'
import { GameBoard } from './components/GameBoard/GameBoard'
import { GameHeader } from './components/GameHeader/GameHeader'
import { previewGame } from './fixtures/previewGame'
import { useSnakeGame } from './hooks/useSnakeGame'

function App() {
  const {
    screen,
    snake,
    food,
    score,
    startGame,
    goToMenu,
  } = useSnakeGame()

  if (screen === 'start') {
    return (
      <StartPage
        onStart={startGame}
      />
    )
  }

  if (screen === 'game_over') {
    return (
      <GameOverPage
        score={score}
        onRestart={startGame}
        onMenu={goToMenu}
      />
    )
  }

  return (
    <main className="game-placeholder">
      <GameHeader score={score} />

      <GameBoard
        boardSize={previewGame.boardSize}
        snake={snake}
        food={food}
      />

      <button
        type="button"
        onClick={startGame}
      >
        RESTART
      </button>
    </main>
  )
}

export default App