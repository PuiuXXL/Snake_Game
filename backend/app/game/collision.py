"""Exercitiul 2: coliziuni cu marginile si corpul."""

from app.models.game import Position


def has_collision(
    next_head: Position,
    snake: list[Position],
    board_size: int,
    *,
    growing: bool = False,
) -> bool:
    """Verifica lovitura cu peretele sau cu corpul.

    Cand sarpele NU mananca, ultima celula din coada se elibereaza
    in acest tick. De aceea nu o consideram obstacol.
    """
    hit_wall = (
        next_head.x < 0
        or next_head.y < 0
        or next_head.x >= board_size
        or next_head.y >= board_size
    )
    body_to_check = snake if growing else snake[:-1]
    hit_snake = next_head in body_to_check
    return hit_wall or hit_snake
