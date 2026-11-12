import type { Direction, GameState } from '../types/game'
import { postJson } from './http'

export function newGame(): Promise<GameState> {
  return postJson<GameState>('/game/new')
}

export function stepGame(
  state: GameState,
  direction: Direction,
): Promise<GameState> {
  return postJson<GameState>('/game/step', { state, direction })
}
