
import deadSnake from '../assets/sarpeleMort.png'
import './GameOverPage.css'

type GameOverPageProps = {
  score: number
  onRestart: () => void
  onMenu: () => void
}

export function GameOverPage({
  score,
  onRestart,
  onMenu,
}: GameOverPageProps) {
  return (
    <main className="game-over-page">
      <div className="game-over-window">
        <div className="game-over-toolbar">
          <span>SNAKE_OS / FATAL ERROR</span>
          <span>ERR_404</span>
        </div>

        <div className="game-over-content">
          <div className="game-over-info">
            <div className="game-over-heading">
              <span className="game-over-alert">
                SYSTEM FAILURE
              </span>

              <h1>GAME OVER</h1>

              <p>SARPELE..</p>
            </div>

            <div className="game-over-terminal">
              <p>&gt; snake.exe stopped working</p>
              <p>&gt; reason: skill issue</p>
              <p>&gt; John.exe: m-ai nenorocit.</p>
            </div>

            <div className="game-over-score">
              <span>FINAL SCORE</span>
              <strong>{score}</strong>
            </div>

            <button
              className="game-over-restart"
              type="button"
              onClick={onRestart}
            >
              ↻ TRY AGAIN
            </button>

            <button
              className="game-over-menu"
              type="button"
              onClick={onMenu}
            >
              ÎNAPOI LA MENIU
            </button>
          </div>

          <div className="game-over-mascot">
            <div className="game-over-mascot-glow" />

            <img
              src={deadSnake}
              alt="Snake mascot defeated"
              draggable={false}
            />

           
          </div>
        </div>
      </div>
    </main>
  )
}
