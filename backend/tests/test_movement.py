from app.game.movement import choose_direction, get_next_head
from app.models.game import Direction, Position


def test_four_directions():
    start = Position(x=5, y=5)
    assert get_next_head(start, Direction.up) == Position(x=5, y=4)
    assert get_next_head(start, Direction.down) == Position(x=5, y=6)
    assert get_next_head(start, Direction.left) == Position(x=4, y=5)
    assert get_next_head(start, Direction.right) == Position(x=6, y=5)
    assert start == Position(x=5, y=5)  # fara mutatii


def test_reject_reverse_direction():
    assert choose_direction(Direction.right, Direction.left) == Direction.right
    assert choose_direction(Direction.right, Direction.up) == Direction.up
