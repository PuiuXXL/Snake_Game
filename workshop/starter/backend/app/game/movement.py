"""ATELIER / TODO 1: calculati miscarea. Solutiile Python sunt comentate."""

from app.models.game import Direction, Position


OPPOSITE = {
    Direction.up: Direction.down,
    Direction.down: Direction.up,
    Direction.left: Direction.right,
    Direction.right: Direction.left,
}


def choose_direction(current: Direction, requested: Direction | None) -> Direction:
    """TODO: Daca directia ceruta este opusa celei curente, pastreaza directia curenta."""
    # if requested is None or requested == OPPOSITE[current]:
    #     return current
    # return requested
    raise NotImplementedError("TODO 1A: alege directia valida")


def get_next_head(head: Position, direction: Direction) -> Position:
    """TODO: Muta capul o singura celula fara a modifica pozitia initiala."""
    # if direction == Direction.up:
    #     return Position(x=head.x, y=head.y - 1)
    # if direction == Direction.down:
    #     return Position(x=head.x, y=head.y + 1)
    # if direction == Direction.left:
    #     return Position(x=head.x - 1, y=head.y)
    # return Position(x=head.x + 1, y=head.y)
    raise NotImplementedError("TODO 1B: calculeaza pozitia capului")
