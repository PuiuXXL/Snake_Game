"""Teste pe niveluri. Ruleaza un nivel:  pytest -k nivel1"""

from game import collisions, engine, food, movement
from game.models import GameState, Position

P = Position


def make_state(**overrides) -> GameState:
    base = dict(
        boardSize=10,
        snake=[P(x=5, y=5), P(x=4, y=5), P(x=3, y=5)],
        direction="right",
        food=P(x=8, y=8),
        score=0,
        status="running",
    )
    base.update(overrides)
    return GameState(**base)


# ---------------------------- NIVEL 1 --------------------------------------
def test_nivel1_next_head_up():
    assert movement.next_head(P(x=5, y=5), "up") == P(x=5, y=4)


def test_nivel1_next_head_down():
    assert movement.next_head(P(x=5, y=5), "down") == P(x=5, y=6)


def test_nivel1_next_head_left():
    assert movement.next_head(P(x=5, y=5), "left") == P(x=4, y=5)


def test_nivel1_next_head_right():
    assert movement.next_head(P(x=5, y=5), "right") == P(x=6, y=5)


# ---------------------------- NIVEL 2 --------------------------------------
def test_nivel2_opposites():
    assert movement.is_opposite("up", "down")
    assert movement.is_opposite("down", "up")
    assert movement.is_opposite("left", "right")
    assert movement.is_opposite("right", "left")


def test_nivel2_not_opposites():
    assert not movement.is_opposite("up", "up")
    assert not movement.is_opposite("up", "left")
    assert not movement.is_opposite("right", "down")


# ---------------------------- NIVEL 3 --------------------------------------
def test_nivel3_inside_board():
    assert not collisions.hits_wall(P(x=0, y=0), 10)
    assert not collisions.hits_wall(P(x=9, y=9), 10)


def test_nivel3_outside_board():
    assert collisions.hits_wall(P(x=-1, y=3), 10)
    assert collisions.hits_wall(P(x=3, y=-1), 10)
    assert collisions.hits_wall(P(x=10, y=3), 10)
    assert collisions.hits_wall(P(x=3, y=10), 10)


# ---------------------------- NIVEL 4 --------------------------------------
def test_nivel4_hits_body():
    assert collisions.hits_self(P(x=4, y=5), [P(x=4, y=5), P(x=3, y=5)])


def test_nivel4_free_cell():
    assert not collisions.hits_self(P(x=6, y=5), [P(x=4, y=5), P(x=3, y=5)])


def test_nivel4_empty_body():
    assert not collisions.hits_self(P(x=1, y=1), [])


# ---------------------------- NIVEL 5 --------------------------------------
def test_nivel5_food_on_free_cell():
    snake = [P(x=5, y=5), P(x=4, y=5), P(x=3, y=5)]
    for _ in range(200):
        cell = food.spawn_food(10, snake)
        assert cell is not None
        assert cell not in snake
        assert 0 <= cell.x < 10 and 0 <= cell.y < 10


def test_nivel5_only_one_free_cell():
    snake = [P(x=0, y=0), P(x=1, y=0), P(x=0, y=1)]
    assert food.spawn_food(2, snake) == P(x=1, y=1)


def test_nivel5_board_full():
    snake = [P(x=0, y=0), P(x=1, y=0), P(x=0, y=1), P(x=1, y=1)]
    assert food.spawn_food(2, snake) is None


# ---------------------------- NIVEL 6 --------------------------------------
def test_nivel6_moves_forward():
    new = engine.step(make_state(), "right")
    assert new.snake == [P(x=6, y=5), P(x=5, y=5), P(x=4, y=5)]
    assert new.status == "running"
    assert new.score == 0


def test_nivel6_does_not_mutate_input():
    state = make_state()
    engine.step(state, "right")
    assert state.snake[0] == P(x=5, y=5)


def test_nivel6_turns():
    new = engine.step(make_state(), "up")
    assert new.direction == "up"
    assert new.snake[0] == P(x=5, y=4)


def test_nivel6_ignores_reverse():
    new = engine.step(make_state(), "left")
    assert new.direction == "right"
    assert new.snake[0] == P(x=6, y=5)


def test_nivel6_eats_food():
    state = make_state(food=P(x=6, y=5))
    new = engine.step(state, "right")
    assert len(new.snake) == 4
    assert new.snake[0] == P(x=6, y=5)
    assert new.score == 10
    assert new.food is not None
    assert new.food != P(x=6, y=5)
    assert new.food not in new.snake


def test_nivel6_wall_game_over():
    state = make_state(snake=[P(x=9, y=5), P(x=8, y=5), P(x=7, y=5)])
    assert engine.step(state, "right").status == "game_over"


def test_nivel6_self_collision_game_over():
    snake = [P(x=5, y=5), P(x=5, y=6), P(x=4, y=6), P(x=4, y=5), P(x=4, y=4)]
    state = make_state(snake=snake, direction="up")
    assert engine.step(state, "left").status == "game_over"


def test_nivel6_moving_into_tail_is_allowed():
    # patrat 2x2: capul intra in celula pe care o paraseste coada
    snake = [P(x=5, y=5), P(x=5, y=6), P(x=4, y=6), P(x=4, y=5)]
    state = make_state(snake=snake, direction="up")
    assert engine.step(state, "left").status == "running"


def test_nivel6_no_move_when_not_running():
    state = make_state(status="game_over")
    assert engine.step(state, "up") == state
