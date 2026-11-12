import type { Direction, Position } from '../types/game'

export const MOVE_INTERVAL_MS = 140

export function getNextHead(
  head: Position,
  direction: Direction,
): Position {
  const nextHead = { ...head }

  if (direction === 'up') nextHead.y -= 1
  if (direction === 'down') nextHead.y += 1
  if (direction === 'left') nextHead.x -= 1
  if (direction === 'right') nextHead.x += 1

  return nextHead
}

export function hasCollision(
  nextHead: Position,
  snake: Position[],
  boardSize: number,
): boolean {
  const hitWall =
    nextHead.x < 0 ||
    nextHead.x >= boardSize ||
    nextHead.y < 0 ||
    nextHead.y >= boardSize

  const hitSnake = snake.some(
    (segment) =>
      segment.x === nextHead.x &&
      segment.y === nextHead.y,
  )

  return hitWall || hitSnake
}

export function getRandomFood(
  snake: Position[],
  boardSize: number,
): Position | null {
  const availablePositions: Position[] = []

  for (let y = 0; y < boardSize; y += 1) {
    for (let x = 0; x < boardSize; x += 1) {
      const occupied = snake.some(
        (segment) => segment.x === x && segment.y === y,
      )

      if (!occupied) {
        availablePositions.push({ x, y })
      }
    }
  }

  if (availablePositions.length === 0) {
    return null
  }

  return availablePositions[
    Math.floor(Math.random() * availablePositions.length)
  ]
}
