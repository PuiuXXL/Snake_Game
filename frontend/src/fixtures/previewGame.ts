import type { GameState } from '../types/game'

export const previewGame: GameState = {
  boardSize: 20,
  snake: [
    { x: 10, y: 9 },
    { x: 9, y: 9 },
    { x: 8, y: 9 },
    { x: 7, y: 9 },
  ],
  direction: 'right',
  food: { x: 14, y: 6 },
  score: 0,
  status: 'ready',
}