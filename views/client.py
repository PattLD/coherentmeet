from datetime import date, datetime
from pydantic import BaseModel

class ClientOut(BaseModel):
    nome: str
    sobrenome: str
    cpf: str
    email: str
    data_nascimento: date
    telefone: str
    cadastro_em: datetime
    