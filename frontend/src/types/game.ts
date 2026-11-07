export type Position = {
  x: number
  y: number
}

export type Direction = 'up' | 'down' | 'left' | 'right'

export type GameStatus = 'ready' | 'running' | 'game_over'

export type GameState = {
  boardSize: number
  snake: Position[]
  direction: Direction
  food: Position | null
  score: number
  status: GameStatus
}