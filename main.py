from contextlib import asynccontextmanager
from fastapi import FastAPI
from controllers import client
from database import database, metadata, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.client import clients #noqa
    metadata.create_all(engine)
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(client.router)
