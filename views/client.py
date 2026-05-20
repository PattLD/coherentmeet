from datetime import date, datetime
from pydantic import BaseModel

class ClientOut(BaseModel):
    name: str
    last_name: str
    cpf: str
    email: str
    birth_date: date
    phone_number: str
    register_at: datetime
    