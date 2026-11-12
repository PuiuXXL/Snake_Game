"""Datele jocului si contractul JSON dintre Python si React."""

from enum import Enum
from pydantic import BaseModel, Field


class Direction(str, Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"


class GameStatus(str, Enum):
    ready = "ready"
    running = "running"
    game_over = "game_over"


class Position(BaseModel):
    x: int
    y: int


class GameState(BaseModel):
    # CamelCase aici pastreaza compatibilitatea cu types/game.ts.
    boardSize: int = Field(ge=5, le=100)
    snake: list[Position]
    direction: Direction
    food: Position | None
    score: int = Field(ge=0)
    status: GameStatus


class StartResponse(BaseModel):
    gameId: str
    state: GameState


class DirectionRequest(BaseModel):
    direction: Direction


class TickRequest(BaseModel):
    # Optional: trimitem ultima tasta impreuna cu tick-ul, fara curse HTTP.
    direction: Direction | None = None
