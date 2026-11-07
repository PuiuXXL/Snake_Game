
import { GameOverPage } from './pages/GameOverPage'
import './App.css'

function App() {
  return (
    <GameOverPage
      score={120}
      onRestart={() => window.location.reload()}
    />
  )
}

export default App
