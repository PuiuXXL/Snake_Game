import { GAME_ASSETS } from '../../config/game'
import type { Position } from '../../types/game'
import './GameBoard.css'

type GameBoardProps = {
  boardSize: number
  snake: Position[]
  food: Position | null
}

export function GameBoard({
  boardSize,
  snake,
  food,
}: GameBoardProps) {
  return (
    <div className="board-frame">
      <div
        className="game-board"
        role="img"
        aria-label={`Tablă Snake de ${boardSize} pe ${boardSize} celule`}
        style={{
          gridTemplateColumns: `repeat(${boardSize}, 1fr)`,
          gridTemplateRows: `repeat(${boardSize}, 1fr)`,
        }}
      >
        {Array.from({ length: boardSize * boardSize }, (_, index) => {
          const x = index % boardSize
          const y = Math.floor(index / boardSize)
          const isLight = (x + y) % 2 === 0

          return (
            <div
              key={`cell-${x}-${y}`}
              className={`board-cell ${isLight ? 'board-cell--light' : ''}`}
              style={{
                gridColumn: x + 1,
                gridRow: y + 1,
              }}
            />
          )
        })}

        {snake.map((segment, index) => (
          <img
            key={`snake-${index}`}
            className="board-sprite"
            src={
              index === 0
                ? GAME_ASSETS.snakeHead
                : GAME_ASSETS.snakeBody
            }
            alt=""
            draggable={false}
            style={{
              gridColumn: segment.x + 1,
              gridRow: segment.y + 1,
            }}
          />
        ))}

        {food && (
          <img
            className="board-sprite"
            src={GAME_ASSETS.food}
            alt=""
            draggable={false}
            style={{
              gridColumn: food.x + 1,
              gridRow: food.y + 1,
            }}
          />
        )}
      </div>
    </div>
  )
}