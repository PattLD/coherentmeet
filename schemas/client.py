from datetime import date, datetime
from pydantic import BaseModel

class ClientIn(BaseModel):
    name: str
    last_name: str
    cpf: str
    email: str
    birth_date: date
    phone_number: str

class ClientUpdateIn(BaseModel):
    name: str | None = None
    last_name: str | None = None
    cpf: str | None = None
    email: str | None = None
    birth_date: date | None = None
    phone_number: str | None = None