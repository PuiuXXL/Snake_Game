import './App.css'
import { StartPage } from './pages/StartPage'
import { GameOverPage } from './pages/GameOverPage'
import { GameBoard } from './components/GameBoard/GameBoard'
import { GameHeader } from './components/GameHeader/GameHeader'
import { useSnakeGame } from './hooks/useSnakeGame'

function App() {
  const {
    screen,
    snake,
    food,
    score,
    boardSize,
    error,
    startGame,
    goToMenu,
  } = useSnakeGame()

  if (screen === 'start') {
    return (
      <>
        <StartPage onStart={() => void startGame()} />
        {error && (
          <div className="api-error" role="alert">
            {error}
          </div>
        )}
      </>
    )
  }

  if (screen === 'game_over') {
    return (
      <GameOverPage
        score={score}
        onRestart={() => void startGame()}
        onMenu={goToMenu}
      />
    )
  }

  return (
    <main className="game-placeholder">
      <GameHeader score={score} />

      <GameBoard
        boardSize={boardSize}
        snake={snake}
        food={food}
      />

      <button
        type="button"
        onClick={() => void startGame()}
      >
        RESTART
      </button>
    </main>
  )
}

export default App
