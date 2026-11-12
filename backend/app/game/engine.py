"""Motorul jocului: combina functiile mici folosite in workshop."""

import random

from app.config import BOARD_SIZE
from app.game.collision import has_collision
from app.game.food import ate_food, get_random_food
from app.game.movement import choose_direction, get_next_head
from app.game.score import update_score
from app.models.game import Direction, GameState, GameStatus, Position


def new_game(board_size: int = BOARD_SIZE, *, rng: random.Random | None = None) -> GameState:
    """Construieste starea initiala pentru un joc nou."""
    if not 5 <= board_size <= 100:
        raise ValueError("board_size trebuie sa fie intre 5 si 100")

    head_x, head_y = max(3, board_size // 2), max(1, board_size // 2 - 1)
    snake = [Position(x=head_x - i, y=head_y) for i in range(4)]

    # Aceeasi pozitie de la preview-ul original, pentru tabla de 20x20.
    preview_food = Position(x=14, y=6) if board_size == 20 else None
    food = preview_food if preview_food is not None else get_random_food(snake, board_size, rng=rng)

    return GameState(
        boardSize=board_size,
        snake=snake,
        direction=Direction.right,
        food=food,
        score=0,
        status=GameStatus.running,
    )


def set_direction(state: GameState, requested: Direction) -> GameState:
    """Schimba doar directia, fara a avansa jocul."""
    if state.status != GameStatus.running:
        return state.model_copy(deep=True)
    return state.model_copy(update={"direction": choose_direction(state.direction, requested)}, deep=True)


def tick(
    state: GameState,
    requested_direction: Direction | None = None,
    *,
    rng: random.Random | None = None,
) -> GameState:
    """Executa exact un pas. Datele de intrare nu sunt modificate."""
    if state.status != GameStatus.running:
        return state.model_copy(deep=True)

    direction = choose_direction(state.direction, requested_direction)
    next_head = get_next_head(state.snake[0], direction)
    ate = ate_food(next_head, state.food)

    if has_collision(next_head, state.snake, state.boardSize, growing=ate):
        return state.model_copy(
            update={"direction": direction, "status": GameStatus.game_over}, deep=True
        )

    new_snake = [next_head, *state.snake] if ate else [next_head, *state.snake[:-1]]
    new_food = get_random_food(new_snake, state.boardSize, rng=rng) if ate else state.food

    return GameState(
        boardSize=state.boardSize,
        snake=new_snake,
        direction=direction,
        food=new_food,
        score=update_score(state.score, ate),
        status=GameStatus.game_over if new_food is None else GameStatus.running,
    )
