from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import config
from app.core.errors import register_error_handlers
from app.routers import game, health


def create_app() -> FastAPI:
    app = FastAPI(title=config.APP_TITLE)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.CORS_ORIGINS,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    register_error_handlers(app)

    app.include_router(health.router)
    app.include_router(game.router)
    return app


app = create_app()
