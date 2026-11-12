"""Exercitiul 4: calculul scorului."""

from app.config import POINTS_PER_FOOD


def update_score(score: int, ate: bool) -> int:
    """Adauga puncte doar cand sarpele consuma mancare."""
    return score + POINTS_PER_FOOD if ate else score
