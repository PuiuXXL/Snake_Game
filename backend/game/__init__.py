"""Pachetul jocului: logica pura, fara FastAPI.

  models.py      - tipurile de date (gata)
  movement.py    - nivelurile 1-2
  collisions.py  - nivelurile 3-4
  food.py        - nivelul 5
  engine.py      - new_game (gata) + step (nivelul 6)
"""

from .collisions import hits_self, hits_wall
from .engine import new_game, step
from .food import spawn_food
from .movement import is_opposite, next_head

__all__ = [
    "hits_self",
    "hits_wall",
    "is_opposite",
    "new_game",
    "next_head",
    "spawn_food",
    "step",
]
