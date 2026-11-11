import { useEffect, useState } from 'react'
import { previewGame } from '../fixtures/previewGame'
import {
  getNextHead,
  getRandomFood,
  hasCollision,
  MOVE_INTERVAL_MS,
} from '../game/gameRules'
import type { Direction, Position } from '../types/game'

export type GameScreen = 'start' | 'game' | 'game_over'

export function useSnakeGame() {
  const [screen, setScreen] = useState<GameScreen>('start')
  const [snake, setSnake] = useState<Position[]>(previewGame.snake)
  const [direction, setDirection] = useState<Direction>(
    previewGame.direction,
  )
  const [score, setScore] = useState(0)
  const [food, setFood] = useState<Position | null>(
    previewGame.food,
  )

  useEffect(() => {
    if (screen !== 'game') {
      return
    }

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

    const handleKeyDown = (event: KeyboardEvent) => {
      const nextDirection = directionByKey[event.key]

      if (!nextDirection) {
        return
      }

      event.preventDefault()

      if (oppositeDirections[direction] !== nextDirection) {
        setDirection(nextDirection)
      }
    }

    window.addEventListener('keydown', handleKeyDown)

    return () => {
      window.removeEventListener('keydown', handleKeyDown)
    }
  }, [direction, screen])

  useEffect(() => {
    if (screen !== 'game') {
      return
    }

    const timer = window.setInterval(() => {
      setSnake((currentSnake) => {
        const nextHead = getNextHead(currentSnake[0], direction)

        if (
          hasCollision(
            nextHead,
            currentSnake,
            previewGame.boardSize,
          )
        ) {
          setScreen('game_over')
          return currentSnake
        }

        const ateFood =
          food?.x === nextHead.x &&
          food?.y === nextHead.y

        if (ateFood) {
          setScore((currentScore) => currentScore + 10)
          setFood(
            getRandomFood(
              [nextHead, ...currentSnake],
              previewGame.boardSize,
            ),
          )
          return [nextHead, ...currentSnake]
        }

        return [nextHead, ...currentSnake.slice(0, -1)]
      })
    }, MOVE_INTERVAL_MS)

    return () => {
      window.clearInterval(timer)
    }
  }, [direction, food, screen])

  const startGame = () => {
    setSnake(previewGame.snake)
    setDirection(previewGame.direction)
    setScore(0)
    setFood(previewGame.food)
    setScreen('game')
  }

  const goToMenu = () => {
    setScreen('start')
  }

  return {
    screen,
    snake,
    food,
    score,
    startGame,
    goToMenu,
  }
}
