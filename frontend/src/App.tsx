import { ErrorBanner } from './components/ErrorBanner/ErrorBanner'
import { GameScreen } from './components/GameScreen/GameScreen'
import { useGame } from './hooks/useGame'
import { useKeyboardControls } from './hooks/useKeyboardControls'
import { GameOverPage } from './pages/GameOverPage'
import { StartPage } from './pages/StartPage'
import './App.css'

function App() {
  const { game, error, loading, start, retry, changeDirection } = useGame()

  useKeyboardControls(game?.status === 'running', changeDirection)

  if (!game) {
    return (
      <>
        <StartPage onStart={start} />
        {loading && <ErrorBanner message="Se conectează la backend…" />}
        {error && <ErrorBanner message={error} />}
      </>
    )
  }

  if (game.status === 'game_over') {
    return <GameOverPage score={game.score} onRestart={start} />
  }

  return (
    <>
      <GameScreen game={game} />
      {error && <ErrorBanner message={error} onRetry={retry} />}
    </>
  )
}

export default App
