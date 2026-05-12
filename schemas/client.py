from datetime import date, datetime
from pydantic import BaseModel

class ClientIn(BaseModel):
    nome: str
    sobrenome: str
    cpf: str
    email: str
    data_nascimento: date
    telefone: str
    created_at: datetime