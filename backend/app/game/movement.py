"""Exercitiul 1: miscarea sarpelui."""

from app.models.game import Direction, Position


OPPOSITE = {
    Direction.up: Direction.down,
    Direction.down: Direction.up,
    Direction.left: Direction.right,
    Direction.right: Direction.left,
}


def choose_direction(current: Direction, requested: Direction | None) -> Direction:
    """Intoarce directia valida; interzice intoarcerea cu 180 de grade."""
    if requested is None or requested == OPPOSITE[current]:
        return current
    return requested


def get_next_head(head: Position, direction: Direction) -> Position:
    """Calculeaza noul cap, fara sa modifice pozitia initiala."""
    if direction == Direction.up:
        return Position(x=head.x, y=head.y - 1)
    if direction == Direction.down:
        return Position(x=head.x, y=head.y + 1)
    if direction == Direction.left:
        return Position(x=head.x - 1, y=head.y)
    return Position(x=head.x + 1, y=head.y)
