"""Exercitiul 3: mancare si crestere."""

import random
from app.models.game import Position


def ate_food(head: Position, food: Position | None) -> bool:
    """Verifica daca noul cap se afla peste mancare."""
    return food is not None and head == food


def get_random_food(
    snake: list[Position], board_size: int, *, rng: random.Random | None = None
) -> Position | None:
    """Alege uniform o celula libera, sau None cand tabla este plina."""
    occupied = {(segment.x, segment.y) for segment in snake}
    free = [
        Position(x=x, y=y)
        for y in range(board_size)
        for x in range(board_size)
        if (x, y) not in occupied
    ]
    if not free:
        return None
    return (rng if rng is not None else random).choice(free)
