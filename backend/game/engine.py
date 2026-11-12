"""Starea jocului: new_game (gata facut) si step (NIVELUL 6).

Ruleaza testele cu:  pytest -k nivel6
"""

from .collisions import hits_self, hits_wall  # noqa: F401
from .food import spawn_food  # noqa: F401
from .models import Direction, GameState, Position
from .movement import is_opposite, next_head  # noqa: F401


# Gata facut (exemplu pentru participanti)
def new_game(board_size: int = 20) -> GameState:
    """Creeaza un joc nou: sarpe de 4 celule in mijloc, mergand spre dreapta.

    Prima mancare e la o pozitie fixa, ca jocul sa porneasca inca de la
    nivelul 1 (fara sa depinda de spawn_food).
    """
    mid = board_size // 2
    return GameState(
        boardSize=board_size,
        snake=[Position(x=mid - i, y=mid) for i in range(4)],
        direction="right",
        food=Position(x=mid + 4, y=mid),
        score=0,
        status="running",
    )


# NIVEL 6 - Un pas de joc (le leaga pe toate)
def step(state: GameState, requested: Direction) -> GameState:
    """Avanseaza jocul cu un pas si intoarce noua stare (un GameState nou).

    Pasi:
      1. Daca state.status nu este "running", intoarce starea neschimbata.
      2. Alege directia: `requested`, dar daca este opusul directiei curente,
         pastreaza directia curenta (foloseste is_opposite).
      3. Calculeaza noul cap (next_head).
      4. Verifica daca a mancat: noul cap == state.food.
      5. Verifica coliziunile: hits_wall si hits_self. Daca NU a mancat, coada
         se muta, deci verifica fata de snake[:-1]; daca a mancat, fata de tot
         corpul. La coliziune intoarce starea cu status="game_over".
      6. Noul sarpe = [noul cap] + sarpele vechi. Daca NU a mancat, scoate
         ultima celula (coada). Daca a mancat, sarpele creste.
      7. Daca a mancat: score + 10 si mancare noua cu spawn_food.
    """
    raise NotImplementedError("Nivel 6: completeaza step (game/engine.py)")
