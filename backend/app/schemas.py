"""Corpurile cererilor API (starea jocului e in game/models.py)."""

from pydantic import BaseModel

from game.models import Direction, GameState


class StepRequest(BaseModel):
    state: GameState
    direction: Direction
