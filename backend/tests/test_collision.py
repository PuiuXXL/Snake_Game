from app.game.collision import has_collision
from app.models.game import Position


def test_walls():
    snake = [Position(x=2, y=2)]
    for head in [Position(x=-1, y=2), Position(x=5, y=2), Position(x=2, y=-1), Position(x=2, y=5)]:
        assert has_collision(head, snake, 5)
    assert not has_collision(Position(x=3, y=2), snake, 5)


def test_body_collision():
    snake = [Position(x=2, y=2), Position(x=1, y=2), Position(x=1, y=3)]
    assert has_collision(Position(x=1, y=2), snake, 5)
    # Coada se muta, daca nu mananca; poate intra pe fosta pozitie a cozii.
    assert not has_collision(Position(x=1, y=3), snake, 5, growing=False)
    assert has_collision(Position(x=1, y=3), snake, 5, growing=True)
