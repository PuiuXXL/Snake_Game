from fastapi import APIRouter, Query

from app.core import config
from app.schemas import StepRequest
from app.services import game_service
from game.models import GameState

router = APIRouter(prefix="/game", tags=["game"])


@router.post("/new", response_model=GameState)
def new_game(
    board_size: int = Query(
        config.DEFAULT_BOARD_SIZE,
        ge=config.MIN_BOARD_SIZE,
        le=config.MAX_BOARD_SIZE,
    ),
) -> GameState:
    return game_service.create_game(board_size)


@router.post("/step", response_model=GameState)
def step(request: StepRequest) -> GameState:
    return game_service.advance_game(request.state, request.direction)
