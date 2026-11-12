"""ATELIER / TODO 3: mancarea. Solutiile executabile sunt comentate."""

import random
from app.models.game import Position


def ate_food(head: Position, food: Position | None) -> bool:
    """TODO: Verifica daca noul cap este pe aceeasi celula ca mancarea."""
    # return food is not None and head == food
    raise NotImplementedError("TODO 3A: detecteaza mancarea")


def get_random_food(
    snake: list[Position], board_size: int, *, rng: random.Random | None = None
) -> Position | None:
    """TODO: Alege o celula libera. Intoarce None daca tabla este plina."""
    # occupied = {(segment.x, segment.y) for segment in snake}
    # free = [
    #     Position(x=x, y=y)
    #     for y in range(board_size)
    #     for x in range(board_size)
    #     if (x, y) not in occupied
    # ]
    # if not free:
    #     return None
    # return (rng if rng is not None else random).choice(free)
    raise NotImplementedError("TODO 3B: genereaza o pozitie libera")
