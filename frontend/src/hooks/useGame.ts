import { useCallback, useEffect, useRef, useState } from 'react'
import { newGame, stepGame } from '../services/gameApi'
import { ApiError } from '../services/http'
import type { Direction, GameState } from '../types/game'

const TICK_MS = 140

const NOT_IMPLEMENTED_MESSAGE =
  'Jocul nu se poate mișca încă: logica din backend nu e completă.'

function messageOf(error: unknown): string {
  if (error instanceof ApiError && error.status === 501) {
    return NOT_IMPLEMENTED_MESSAGE
  }
  return error instanceof Error ? error.message : 'Eroare necunoscută'
}

export function useGame() {
  const [game, setGame] = useState<GameState | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)
  const directionRef = useRef<Direction>('right')

  const start = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const state = await newGame()
      directionRef.current = state.direction
      setGame(state)
    } catch (e) {
      setGame(null)
      setError(messageOf(e))
    } finally {
      setLoading(false)
    }
  }, [])

  const changeDirection = useCallback((direction: Direction) => {
    directionRef.current = direction
  }, [])

  // Reia jocul după o eroare de pas (ex. după ce ai completat o funcție).
  const retry = useCallback(() => setError(null), [])

  // Un singur request în zbor: următorul pas se programează abia după
  // ce a sosit starea nouă. La eroare jocul rămâne pe ecran, înghețat.
  useEffect(() => {
    if (!game || game.status !== 'running' || error) return

    let cancelled = false
    const timer = setTimeout(async () => {
      try {
        const next = await stepGame(game, directionRef.current)
        if (!cancelled) setGame(next)
      } catch (e) {
        if (!cancelled) setError(messageOf(e))
      }
    }, TICK_MS)

    return () => {
      cancelled = true
      clearTimeout(timer)
    }
  }, [game, error])

  return { game, error, loading, start, retry, changeDirection }
}
