from pydantic import BaseModel


class ClienteBase(BaseModel):
    nome: str
    cpfcnpj: str
    email: str


class ClienteCreate(ClienteBase):
    pass

# class User(UserBase):
#     id: int
#     is_active: bool
#     class Config:
#         orm_mode = True