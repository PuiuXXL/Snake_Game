"""Regulile si configuratia utilizate de serverul Python."""

import os

BOARD_SIZE = 20
MOVE_INTERVAL_MS = 140
POINTS_PER_FOOD = 10

# React ruleaza pe portul 5173 in dezvoltare.
FRONTEND_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173"
    ).split(",")
    if origin.strip()
]
