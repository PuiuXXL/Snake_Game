import { useCallback, useEffect, useRef, useState } from 'react'
import { previewGame } from '../fixtures/previewGame'
import { gameApi } from '../services/gameApi'
import type { Direction, GameState } from '../types/game'

export type GameScreen = 'start' | 'game' | 'game_over'

// UI-ul se ocupa doar de tastatura, timer si afisare.
// Python decide miscarea, mancarea, coliziunile si scorul.
const MOVE_INTERVAL_MS = 140

const directionByKey: Record<string, Direction> = {
  ArrowUp: 'up',
  w: 'up',
  ArrowDown: 'down',
  s: 'down',
  ArrowLeft: 'left',
  a: 'left',
  ArrowRight: 'right',
  d: 'right',
}

const oppositeDirections: Record<Direction, Direction> = {
  up: 'down',
  down: 'up',
  left: 'right',
  right: 'left',
}

export function useSnakeGame() {
  const [screen, setScreen] = useState<GameScreen>('start')
  const [game, setGame] = useState<GameState>(previewGame)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const gameIdRef = useRef<string | null>(null)
  const directionRef = useRef<Direction>(previewGame.direction)
  const inFlightRef = useRef(false)
  // O cerere veche nu are voie sa suprascrie o sesiune noua.
  const sessionVersionRef = useRef(0)

  const startGame = useCallback(async () => {
    const version = ++sessionVersionRef.current
    setLoading(true)
    setError(null)
    gameIdRef.current = null

    try {
      const session = await gameApi.start()
      if (sessionVersionRef.current !== version) return
      gameIdRef.current = session.gameId
      directionRef.current = session.state.direction
      setGame(session.state)
      setScreen('game')
    } catch (caught) {
      if (sessionVersionRef.current !== version) return
      setError(caught instanceof Error ? caught.message : 'Eroare necunoscuta de conexiune.')
      setScreen('start')
    } finally {
      if (sessionVersionRef.current === version) setLoading(false)
    }
  }, [])

  const goToMenu = useCallback(() => {
    ++sessionVersionRef.current
    gameIdRef.current = null
    setScreen('start')
    setError(null)
    setLoading(false)
  }, [])

  useEffect(() => {
    if (screen !== 'game') return

    const onKeyDown = (event: KeyboardEvent) => {
      const key = event.key.startsWith('Arrow') ? event.key : event.key.toLowerCase()
      const nextDirection = directionByKey[key]
      if (!nextDirection) return

      event.preventDefault()
      if (oppositeDirections[directionRef.current] !== nextDirection) {
        directionRef.current = nextDirection
      }
    }

    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [screen])

  useEffect(() => {
    if (screen !== 'game') return

    const timer = window.setInterval(() => {
      const gameId = gameIdRef.current
      if (!gameId || inFlightRef.current) return

      const version = sessionVersionRef.current
      inFlightRef.current = true

      void gameApi.tick(gameId, directionRef.current)
        .then((updated) => {
          if (sessionVersionRef.current !== version) return
          setGame(updated)
          if (updated.status === 'game_over') setScreen('game_over')
        })
        .catch((caught) => {
          if (sessionVersionRef.current !== version) return
          setError(caught instanceof Error ? caught.message : 'Eroare la actualizarea jocului.')
          setScreen('start')
        })
        .finally(() => {
          inFlightRef.current = false
        })
    }, MOVE_INTERVAL_MS)

    return () => window.clearInterval(timer)
  }, [screen])

  return {
    screen,
    snake: game.snake,
    food: game.food,
    score: game.score,
    boardSize: game.boardSize,
    loading,
    error,
    startGame,
    goToMenu,
  }
}
