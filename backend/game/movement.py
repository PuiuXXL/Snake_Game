"""NIVELURILE 1-2: miscarea sarpelui.

Reminder: originea (0, 0) este in COLTUL DIN STANGA-SUS.
  * "up"    scade y        * "down"  creste y
  * "left"  scade x        * "right" creste x

Nu modifica semnaturile functiilor si nu modifica argumentele primite.
Ruleaza testele cu:  pytest -k nivel1
"""

from .models import Direction, Position


# NIVEL 1 - Miscarea capului
def next_head(head: Position, direction: Direction) -> Position:
    """Intoarce pozitia in care ajunge capul dupa un pas in `direction`.

    Exemplu: next_head(Position(x=5, y=5), "up") -> Position(x=5, y=4)
    """
    raise NotImplementedError("Nivel 1: completeaza next_head (game/movement.py)")


# NIVEL 2 - Schimbarea directiei
def is_opposite(current: Direction, requested: Direction) -> bool:
    """True daca `requested` este exact opusul lui `current`.

    Sarpele nu are voie sa se intoarca pe loc (ex: din "left" in "right").
    Exemplu: is_opposite("up", "down") -> True ; is_opposite("up", "left") -> False
    """
    raise NotImplementedError("Nivel 2: completeaza is_opposite (game/movement.py)")
