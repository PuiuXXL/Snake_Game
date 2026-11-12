import type { Direction, GameSession, GameState } from '../types/game'

// In dezvoltare, Python ruleaza la portul 8000, iar Vite la 5173.
const API_BASE = (import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000').replace(/\/$/, '')

async function request<T>(path: string, method: 'GET' | 'POST' = 'GET', body?: unknown): Promise<T> {
  let response: Response
  try {
    response = await fetch(`${API_BASE}${path}`, {
      method,
      headers: { 'Content-Type': 'application/json' },
      ...(body === undefined ? {} : { body: JSON.stringify(body) }),
    })
  } catch {
    throw new Error('Nu pot contacta backend-ul Python. Porneste FastAPI pe portul 8000.')
  }

  if (!response.ok) {
    throw new Error(`Backend-ul a raspuns cu eroarea ${response.status}.`)
  }

  return (await response.json()) as T
}

export const gameApi = {
  start: () => request<GameSession>('/api/game/start', 'POST'),
  get: (gameId: string) => request<GameState>(`/api/game/${gameId}`),
  direction: (gameId: string, direction: Direction) =>
    request<GameState>(`/api/game/${gameId}/direction`, 'POST', { direction }),
  tick: (gameId: string, direction: Direction) =>
    request<GameState>(`/api/game/${gameId}/tick`, 'POST', { direction }),
  reset: (gameId: string) => request<GameState>(`/api/game/${gameId}/reset`, 'POST'),
}
