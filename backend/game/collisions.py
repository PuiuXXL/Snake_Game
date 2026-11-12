"""NIVELURILE 3-4: coliziuni.

Ruleaza testele cu:  pytest -k nivel3
"""

from .models import Position


# NIVEL 3 - Coliziunea cu peretele
def hits_wall(head: Position, board_size: int) -> bool:
    """True daca `head` este in afara tablei.

    Celulele valide au x si y intre 0 si board_size - 1 (inclusiv).
    """
    raise NotImplementedError("Nivel 3: completeaza hits_wall (game/collisions.py)")


# NIVEL 4 - Coliziunea cu propriul corp
def hits_self(head: Position, body: list[Position]) -> bool:
    """True daca `head` se afla pe una dintre celulele din `body`."""
    raise NotImplementedError("Nivel 4: completeaza hits_self (game/collisions.py)")
