# app/Schemas/Cliente.py
from pydantic import BaseModel

class ClienteBase(BaseModel):
    nome: str
    cpfcnpj: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResource(ClienteBase):
    id: int
    class Config:
        from_attributes = True
