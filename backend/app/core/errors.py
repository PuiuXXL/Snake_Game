"""Transforma erorile din logica in raspunsuri HTTP clare."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def register_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(NotImplementedError)
    async def not_implemented_handler(
        _request: Request, error: NotImplementedError
    ) -> JSONResponse:
        # Functia din workshop nu a fost completata inca.
        return JSONResponse(
            status_code=501,
            content={"detail": f"Neimplementat inca: {error}"},
        )
