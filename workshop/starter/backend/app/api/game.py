"""Endpoint-uri apelate de frontend/src/services/gameApi.ts."""

from fastapi import APIRouter, HTTPException

from app.models.game import DirectionRequest, GameState, StartResponse, TickRequest
from app.store import store

router = APIRouter(prefix="/api/game", tags=["Snake"])


def missing_game(game_id: str) -> HTTPException:
    return HTTPException(status_code=404, detail=f"Jocul {game_id} nu exista. Porneste unul nou.")


@router.post("/start", response_model=StartResponse)
def start_game() -> StartResponse:
    game_id, state = store.create()
    return StartResponse(gameId=game_id, state=state)


@router.get("/{game_id}", response_model=GameState)
def get_game(game_id: str) -> GameState:
    try:
        return store.get(game_id)
    except KeyError:
        raise missing_game(game_id) from None


@router.post("/{game_id}/direction", response_model=GameState)
def change_direction(game_id: str, payload: DirectionRequest) -> GameState:
    try:
        return store.change_direction(game_id, payload.direction)
    except KeyError:
        raise missing_game(game_id) from None


@router.post("/{game_id}/tick", response_model=GameState)
def advance_game(game_id: str, payload: TickRequest | None = None) -> GameState:
    try:
        return store.advance(game_id, payload.direction if payload else None)
    except KeyError:
        raise missing_game(game_id) from None


@router.post("/{game_id}/reset", response_model=GameState)
def reset_game(game_id: str) -> GameState:
    try:
        return store.reset(game_id)
    except KeyError:
        raise missing_game(game_id) from None
