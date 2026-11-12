"""Punct de intrare:  uvicorn main:app --reload --port 8000

Aplicatia propriu-zisa e in app/ (rute, servicii, setari); logica
jocului, pe care o completeaza participantii, e in game/.
"""

from app.main import app

__all__ = ["app"]
