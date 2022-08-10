from fastapi import FastAPI
import uvicorn

from src.db.base import database
from src.core.config import config
from src.endpoints import messages, pages


def setup_routers(app: FastAPI):
    app.include_router(messages.router)
    app.include_router(pages.router)


app = FastAPI(title="Disposable Messages")
setup_routers(app)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=int(config.get("SERVER_PORT")), host=config.get("SERVER_HOST"), reload=True)
