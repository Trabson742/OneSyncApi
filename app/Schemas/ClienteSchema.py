# app/Schemas/Cliente.py
from pydantic import BaseModel

class ClienteSchema():
    class ClienteBase(BaseModel):
        name: str
        cpfcnpj: str
        email: str

    class ClienteCreate(ClienteBase):
        pass

    class ClienteResource(ClienteBase):
        id: int
        class Config:
            from_attributes = True
