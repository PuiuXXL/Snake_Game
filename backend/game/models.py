"""Modelele de date. Oglindesc exact tipurile din frontend/src/types/game.ts.

Acest fisier este deja gata - participantii NU trebuie sa-l modifice.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict

Direction = Literal["up", "down", "left", "right"]
GameStatus = Literal["ready", "running", "game_over"]


class Position(BaseModel):
    """O celula de pe tabla. x = coloana (0 = stanga), y = randul (0 = sus)."""

    model_config = ConfigDict(frozen=True)  # pozitiile se pot compara cu ==

    x: int
    y: int


class GameState(BaseModel):
    boardSize: int
    snake: list[Position]  # snake[0] este capul
    direction: Direction
    food: Position | None
    score: int
    status: GameStatus
