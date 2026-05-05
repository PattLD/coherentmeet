from fastapi import FastAPI

from controllers import client

app = FastAPI()
app.include_router(client.router)