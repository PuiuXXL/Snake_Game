"""Strat intre rute si logica jocului. Rutele nu apeleaza direct `game`."""

from game import engine
from game.models import Direction, GameState


def create_game(board_size: int) -> GameState:
    return engine.new_game(board_size)


def advance_game(state: GameState, direction: Direction) -> GameState:
    return engine.step(state, direction)
