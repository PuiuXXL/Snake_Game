
import sarpele from '../assets/sarpele.png'
import './StartPage.css'

type StartPageProps = {
  onStart: () => void
}

const previewCells = Array.from(
  { length: 100 },
  (_, index) => index
)

const snakeCells = [44, 45, 46, 47, 48]
const snakeHead = 48
const foodCell = 64
const bonusCell = 29

export function StartPage({ onStart }: StartPageProps) {
  return (
    <main className="start-page">
      <section className="start-layout">

        {/* LEFT SIDE */}
        <div className="start-left">

          <div className="title-block">
            <h1 className="title-main">Şarpele</h1>
            <h2 className="title-accent">năzdravan</h2>
          </div>

          <p className="insert-text">
            PRESS START TO PLAY
          </p>

          <button
            className="start-cta"
            type="button"
            onClick={onStart}
          >
            <span className="start-cta__icon">▶</span>
            <span>START GAME</span>
          </button>

          {/* SNAKE MASCOT */}
          <div className="snake-showcase">
            <div className="snake-showcase__glow" />

            <img
              className="snake-showcase__image"
              src={sarpele}
              alt="Snake Overflow mascot"
              draggable={false}
            />
          </div>

        </div>

        {/* RIGHT SIDE */}
        <div className="start-right">
          <div className="preview-board-frame">
            <div
              className="preview-board"
              role="img"
              aria-label="Decorative Snake game preview"
            >
              {previewCells.map((cellIndex) => {
                const isSnake = snakeCells.includes(cellIndex)
                const isHead = cellIndex === snakeHead
                const isFood = cellIndex === foodCell
                const isBonus = cellIndex === bonusCell

                return (
                  <div
                    key={cellIndex}
                    className={[
                      'preview-cell',
                      isSnake ? 'preview-cell--snake' : '',
                      isHead ? 'preview-cell--head' : '',
                      isFood ? 'preview-cell--food' : '',
                      isBonus ? 'preview-cell--bonus' : '',
                    ]
                      .filter(Boolean)
                      .join(' ')}
                  />
                )
              })}
            </div>
          </div>
        </div>

      </section>
    </main>
  )
}
