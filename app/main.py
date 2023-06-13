from fastapi import FastAPI
from app.routers import users


def app() -> FastAPI:
    app = FastAPI()

    app.include_router(users.router)

    return app
