from contextlib import asynccontextmanager
import databases
from fastapi import FastAPI
from controllers import client
import sqlalchemy as sa

DATABASE_URL = "sqlite:///./coherentmeet.db"

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.client import clients #noqa
    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(client.router)
