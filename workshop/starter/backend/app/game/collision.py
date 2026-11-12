"""ATELIER / TODO 2: coliziuni. Solutia executabila este comentata."""

from app.models.game import Position


def has_collision(
    next_head: Position,
    snake: list[Position],
    board_size: int,
    *,
    growing: bool = False,
) -> bool:
    """TODO: Intoarce True daca sarpele loveste un perete sau propriul corp.

    Observatie: atunci cand nu mananca, coada se misca in acest tick.
    Daca mananca (growing=True), coada nu se elibereaza.
    """
    # hit_wall = (
    #     next_head.x < 0
    #     or next_head.y < 0
    #     or next_head.x >= board_size
    #     or next_head.y >= board_size
    # )
    # body_to_check = snake if growing else snake[:-1]
    # hit_snake = next_head in body_to_check
    # return hit_wall or hit_snake
    raise NotImplementedError("TODO 2: verifica coliziunile")
