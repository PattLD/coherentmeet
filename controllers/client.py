

from typing import Annotated
from fastapi import APIRouter, Cookie, Header, Response, status
from schemas.client import ClientIn
from views.client import ClientOut

router = APIRouter(prefix="/clients")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClientOut)
def create_client(client: ClientIn):
    # fake_db.append(client.model_dump())
    return client

@router.get("/", response_model=list[ClientOut])
def read_clients(
    response: Response,
    limit: int = 20,
    skip: int = 0
):
    return []

@router.get("/{client_id}", response_model=ClientOut)
def read_client_id(client_id: int):
    pass