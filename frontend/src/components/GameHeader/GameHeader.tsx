import './GameHeader.css'

type GameHeaderProps = {
  score: number
}

export function GameHeader({ score }: GameHeaderProps) {
  return (
    <header className="game-header">
      <div>
        <p className="game-header__subtitle">PYTHON WORKSHOP</p>
        <h1 className="game-header__title">Snake</h1>
      </div>

      <div className="score-card">
        <span className="score-card__label">SCOR</span>
        <strong className="score-card__value">{score}</strong>
      </div>
    </header>
  )
}