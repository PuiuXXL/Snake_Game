import random
from app.game.engine import new_game, tick
from app.models.game import Direction, GameState, GameStatus, Position


def test_new_game_matches_original_frontend_preview():
    state = new_game()
    assert state.boardSize == 20
    assert state.snake[0] == Position(x=10, y=9)
    assert state.food == Position(x=14, y=6)
    assert state.status == GameStatus.running


def test_tick_moves_snake_without_mutating_old_state():
    state = new_game()
    updated = tick(state)
    assert updated.snake[0] == Position(x=11, y=9)
    assert len(updated.snake) == len(state.snake)
    assert state.snake[0] == Position(x=10, y=9)


def test_tick_eats_and_grows():
    state = new_game()
    state.food = Position(x=11, y=9)
    result = tick(state, rng=random.Random(2))
    assert len(result.snake) == len(state.snake) + 1
    assert result.score == 10
    assert result.food not in result.snake


def test_wall_collision_causes_game_over():
    state = GameState(boardSize=5, snake=[Position(x=4, y=2)], direction=Direction.right,
                      food=Position(x=0, y=0), score=0, status=GameStatus.running)
    result = tick(state)
    assert result.status == GameStatus.game_over
    assert result.snake == state.snake
    assert tick(result).status == GameStatus.game_over


def test_filled_board_ends_game_after_eating():
    state = GameState(
        boardSize=5,
        snake=[Position(x=x, y=y) for y in range(5) for x in range(5) if (x, y) != (4, 4)],
        direction=Direction.right,
        food=Position(x=4, y=4),
        score=0,
        status=GameStatus.running,
    )
    # Construit special cu capul adiacent mancarii, fara ciocnire.
    state.snake.remove(Position(x=3, y=4))
    state.snake.insert(0, Position(x=3, y=4))
    result = tick(state)
    assert result.score == 10
    assert result.food is None
    assert result.status == GameStatus.game_over
