
from services.client import ClientServices
from typing import Annotated
from fastapi import APIRouter, Cookie, Header, Response, status
from models.client import clients
from schemas.client import ClientIn, ClientUpdateIn
from views.client import ClientOut
from database import database

router = APIRouter(prefix="/clients")
services = ClientServices()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClientOut)
async def create_client(client: ClientIn):
    return await services.create(client)

@router.patch("/{client_id}", response_model=ClientOut)
async def update_client(client_id: int, client: ClientUpdateIn):
    return await services.update(client_id,client)

@router.get("/", response_model=list[ClientOut])
async def read_clients(limit: int = 20, skip: int = 0):
    return await services.read_all(limit,skip)

@router.get("/{client_id}", response_model=ClientOut)
async def read_client_id(client_id: int):
    return await services.read_id(client_id)

@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_client(client_id: int):
    return await services.delete(client_id)