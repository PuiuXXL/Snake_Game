"""Jocuri active tinute temporar in memorie (fara baza de date)."""

from threading import RLock
from uuid import uuid4

from app.game.engine import new_game, set_direction, tick
from app.models.game import Direction, GameState


class GameStore:
    def __init__(self) -> None:
        self._lock = RLock()
        self._games: dict[str, GameState] = {}

    def create(self) -> tuple[str, GameState]:
        with self._lock:
            game_id = str(uuid4())
            state = new_game()
            self._games[game_id] = state
            return game_id, state.model_copy(deep=True)

    def get(self, game_id: str) -> GameState:
        with self._lock:
            return self._games[game_id].model_copy(deep=True)

    def change_direction(self, game_id: str, direction: Direction) -> GameState:
        with self._lock:
            state = set_direction(self._games[game_id], direction)
            self._games[game_id] = state
            return state.model_copy(deep=True)

    def advance(self, game_id: str, direction: Direction | None = None) -> GameState:
        with self._lock:
            state = tick(self._games[game_id], direction)
            self._games[game_id] = state
            return state.model_copy(deep=True)

    def reset(self, game_id: str) -> GameState:
        with self._lock:
            if game_id not in self._games:
                raise KeyError(game_id)
            state = new_game()
            self._games[game_id] = state
            return state.model_copy(deep=True)


store = GameStore()
