

from typing import Annotated
from fastapi import APIRouter, Cookie, Header, Response, status
from schemas.client import ClientIn
from views.client import ClientOut

router = APIRouter(prefix="/clients")

fake_db = [
    {"name": "Patricia", "last_name": "Duarte", "birth_date": "2000-10-23", "email": "patricia@gmail.com"},
    {"name": "Ivalter", "last_name": "Duarte", "birth_date": "2005-05-28", "email": "ivalter@gmail.com"},
    {"name": "Natanael", "last_name": "Duarte", "birth_date": "1969-11-23", "email": "natanael@gmail.com"},
    {"name": "Ivone", "last_name": "Duarte", "birth_date": "1972-12-21", "email": "ivone@gmail.com"}
]

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClientOut)
def create_client(client: ClientIn):
    fake_db.append(client.model_dump())
    return client

@router.get("/", response_model=list[ClientOut])
def read_clients(
    response: Response,
    limit: int = 20,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    response.set_cookie(key="user", value="patricia@gmail.com")
    print(f"Cookie: {ads_id}")
    print(f"User_agent: {user_agent}")
    tail = skip + limit
    return [post for post in fake_db[skip:tail]]

@router.get("/{client_id}", response_model=ClientOut)
def read_client_id(client_id: int):
    pass