from app.game.score import update_score


def test_score():
    assert update_score(0, False) == 0
    assert update_score(0, True) == 10
    assert update_score(30, True) == 40
