"""NIVELUL 5: mancarea.

Ruleaza testele cu:  pytest -k nivel5
"""

import random  # noqa: F401  (folosit de participanti la spawn_food)

from .models import Position


# NIVEL 5 - Mancarea
def spawn_food(board_size: int, snake: list[Position]) -> Position | None:
    """Alege o celula LIBERA (care nu e ocupata de sarpe) pentru mancare.

    Intoarce None daca nu mai exista nicio celula libera.
    Indiciu: construieste lista celulelor libere, apoi random.choice(...).
    """
    raise NotImplementedError("Nivel 5: completeaza spawn_food (game/food.py)")
