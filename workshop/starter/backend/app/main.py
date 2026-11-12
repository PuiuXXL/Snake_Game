"""Punctul de intrare FastAPI: python -m uvicorn app.main:app --reload."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.game import router as game_router
from app.config import FRONTEND_ORIGINS

app = FastAPI(title="Snake Overflow - Python Workshop", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(game_router)


@app.get("/api/hello")
def hello() -> dict[str, str]:
    """Primul exercitiu: React primeste un mesaj de la Python."""
    return {"message": "Salut din Python!"}


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
