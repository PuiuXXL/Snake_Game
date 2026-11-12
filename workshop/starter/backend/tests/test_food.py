import random
from app.game.food import ate_food, get_random_food
from app.models.game import Position


def test_ate_food():
    assert ate_food(Position(x=1, y=2), Position(x=1, y=2))
    assert not ate_food(Position(x=1, y=2), Position(x=0, y=2))
    assert not ate_food(Position(x=1, y=2), None)


def test_food_in_free_cell():
    snake = [Position(x=x, y=y) for y in range(3) for x in range(3) if (x, y) != (2, 1)]
    assert get_random_food(snake, 3, rng=random.Random(1)) == Position(x=2, y=1)
    assert get_random_food(snake + [Position(x=2, y=1)], 3) is None
