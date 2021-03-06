# project/app/main.py


import logging

from fastapi import FastAPI

from app.api import ping, players, events
from app.db import init_db

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(players.router, prefix="/players", tags=["players"])
    application.include_router(events.router, prefix="/events", tags=["events"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
